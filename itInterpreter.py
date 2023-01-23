from matplotlib.pyplot import isinteractive
import AST
from AST import addToClass
from functools import reduce

operations = {
    "+" : lambda x, y : x + y,
    "-" : lambda x, y : x - y,
    "*" : lambda x, y : x * y,
    "/" : lambda x, y : x / y,
    "%" : lambda x, y : x % y,
}

comparison_ops = {
    "<" : lambda x , y : x < y,
    ">" : lambda x , y : x > y,
    "<=" : lambda x , y : x <= y,
    ">=" : lambda x , y : x >= y,
    "==" : lambda x , y : x == y,
    "!=" : lambda x , y : x != y,
}

stack = []
vars = { }
functions = { }

def valueOfToken(t):
    if isinstance(t, str):
        if t in vars:
            return vars[t]
    return t

def execute(node):
    while node:
        if node.__class__ in [AST.EntryNode]:
            pass
        elif node.__class__ == AST.ProgramNode:
            if node.parent.__class__ == AST.FunctionDefinitionNode:
                # If the function has to be called multiple times
                if len(node.next) > 1:
                    # Get the function name
                    funcName = node.parent.children[0].tok
                    function = functions[funcName]
                    
                    if len(function.nodes_that_call) > 1:
                        # If the last node that called the function is not the same as the last node in the call stack
                        if function.nodes_that_call[-1] != function.calls_stack[-2]:
                            # Choose the next options in the threading
                            node = node.next[len(function.nodes_that_call) - 1]
                            continue
                    
        elif node.__class__ == AST.TokenNode:
            stack.append(node.tok)
        elif node.__class__ == AST.PrintNode:
            val = stack.pop()
            print(valueOfToken(val))
        elif node.__class__ == AST.OpNode:
            arg2 = valueOfToken(stack.pop())
            if node.nbargs == 2:
                arg1 = valueOfToken(stack.pop())
            else:
                arg1 = 0
                
            # Check if both arguments are numbers
            if isinstance(arg1, int) and isinstance(arg2, int):
                stack.append(operations[node.op](arg1, arg2))
            else:
                print("*** Error : cannot perform operation %s on %s and %s" % (node.op, arg1, arg2))
                return
        
        elif node.__class__ == AST.AssignNode:
            val = valueOfToken(stack.pop())
            name = stack.pop()
            vars[name] = val
        elif node.__class__ == AST.WhileNode:
            cond = valueOfToken(stack.pop())
            if cond:
                node = node.next[0]
            else:
                node = node.next[1]
            continue
        elif node.__class__ == AST.ComparisonNode:
            arg2 = valueOfToken(stack.pop())
            arg1 = valueOfToken(stack.pop())
            op = stack.pop()
            val = comparison_ops[op](arg1, arg2)
            stack.append(val)
        elif node.__class__ == AST.IfNode:
            cond = valueOfToken(stack.pop())
            if cond:
                node = node.next[0]
            else:
                node = node.next[1]
            continue
        elif node.__class__ == AST.ForNode:
            cond = valueOfToken(stack.pop())
            if cond:
                node = node.next[0]
            else:
                node = node.next[1]
            continue
        elif node.__class__ == AST.IntegerNode:
            # Check if the token is a integer
            try:
                int(node.tok)
            except ValueError:
                print("Token %s is not a integer" % node.tok)
            
            stack.append(node.tok)
        elif node.__class__ == AST.StringNode:
            stack.append(node.tok)
        elif node.__class__ == AST.FunctionDefinitionNode:
            # stack.append(node)
            functions[node.children[0].tok] = node
        elif node.__class__ == AST.FunctionCallNode:
            args = []
                        
            # Pop the stack until we find the function name
            for i in range(node.nbargs - 1):
                args.append(valueOfToken(stack.pop()))
                
            # Remove the function name from the stack
            functionName = stack.pop()
            
            # If the function is not defined, raise an error
            if functionName not in functions:
                print("Function %s is not defined" % functionName)
            
            function = functions[functionName]
            
            # Get the function args names
            functionArgsNames = function.children[1:-1]
            
            # Save the current vars values
            for arg in functionArgsNames:
                vars[arg.tok] = args.pop()
                
            nodeSave = node
                    
            if nodeSave not in function.nodes_that_call:
                function.nodes_that_call.append(nodeSave)
                
            function.calls_stack.append(nodeSave)
                    
        if node.next:
            node = node.next[0]
        else:
            node = None

if __name__ == "__main__":
    from banger_parser import parse
    from threader import thread
    import sys
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    entry = thread(ast)
    execute(entry)