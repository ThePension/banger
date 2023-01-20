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

def valueOfToken(t):
    if isinstance(t, str):
        try:
            return vars[t]
        except KeyError:
            print("*** Error : variable %s undefined ! " % t)
    return t

def execute(node):
    while node:
        if node.__class__ in [AST.EntryNode, AST.ProgramNode]:
            pass
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
            stack.append(operations[node.op](arg1, arg2))
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
            print("Comparison result: %s" % val)
            stack.append(val)
        elif node.__class__ == AST.IfNode:
            cond = valueOfToken(stack.pop())
            print("If condition: %s" % cond)
            if cond:
                node = node.next[0]
            else:
                node = node.next[1]
            continue
        elif node.__class__ == AST.ForNode:
            val = valueOfToken(stack.pop())
            name = stack.pop()
            vars[name] = val
            node = node.next[0]
            continue
        elif node.__class__ == AST.IntegerNode:
            stack.append(node.tok)
        elif node.__class__ == AST.StringNode:
            stack.append(node.tok)
        elif node.__class__ == AST.FunctionDefinitionNode:
            stack.append(node)
        elif node.__class__ == AST.FunctionCallNode:
            function = valueOfToken(stack.pop())
            args = []
            for i in range(function.nbargs):
                args.append(valueOfToken(stack.pop()))
            stack.append(function.execute(args))
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