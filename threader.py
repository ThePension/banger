import AST
from AST import ProgramNode, addToClass

entry = None

functions_def_threaded = {}
functions_def_non_threaded = {}
function_calls_stack = []

def getNextNodeRec(currentNode, parentNode):
    if parentNode == None or currentNode not in parentNode.children:
        return None
    currentNodeIndex = parentNode.children.index(currentNode)
    if currentNodeIndex + 1 < len(parentNode.children):
        return parentNode.children[currentNodeIndex + 1]
    else:
        # return getNextNodeRec(parentNode, getParentNode(parentNode))
        return getNextNodeRec(parentNode, parentNode.parent)


@addToClass(AST.WhileNode)
def thread(self, lastNode):
    beforeCondition = lastNode
    conditionNode = self.children[0] # first child
    programNode = self.children[1] # second child

    # Go through the condition to get the last node
    lastNode = conditionNode.thread(lastNode)

    # From the last node of the condition, go to the while, instead of program
    lastNode.addNext(self)

    # From the while, go through the program to get the last node (should be programNode)
    lastNode = programNode.thread(self) # lastNode == programNode
    
    # Program is done
    # From the program return to the condition (which is the last "next node" of the node before the condition)
    lastNode.addNext(beforeCondition.next[-1])

    return self

@addToClass(AST.Node)
def thread(self, lastNode):
    for c in self.children:
        lastNode = c.thread(lastNode)

    lastNode.addNext(self)
    return self

@addToClass(AST.IfNode)
def thread(self, lastNode):
    beforeCondition = lastNode
    conditionNode = self.children[0]
    
    # Go through the condition to get the last node
    lastNode = conditionNode.thread(lastNode)
    
    # From the last node of the condition, go to the if, instead of program
    lastNode.addNext(self)
    
    programNode = self.children[1]
    
    # From the if, go through the program to get the last node (should be programNode)
    lastNode = programNode.thread(self)
    
    # program is done
    # From the program return to the following node
    nextNode = getNextNodeRec(self, self.parent)
        
    if nextNode:
        nextNode.thread(lastNode)
    
    return self

@addToClass(AST.ForNode)
def thread(self, lastNode):
    beforeAssign = lastNode
    assignNode = self.children[0]
    comparisonNode = self.children[1]
    expressionNode = self.children[2]
    programNode = self.children[3]

    # Go through the assignation to get the last node
    lastNode = assignNode.thread(lastNode)

    # Go through the comparison to get the last node
    lastNode = comparisonNode.thread(lastNode)
    
    # From the last node of the comparison, go to the for Node (to test the condition)
    lastNode.addNext(self)

    # From the for Node, go through the program to get the last node (should be programNode)
    lastNode = programNode.thread(self)

    # Go through the expression to get the last node
    lastNode = expressionNode.thread(lastNode)
    
    # From the last node of the expression, go back to the comparison
    lastNode.addNext(assignNode.next[-1])
    
    return self

@addToClass(AST.FunctionDefinitionNode)
def thread(self, lastNode):
    functionNameNode = self.children[0]
    lastNode = functionNameNode.thread(lastNode)
    
    # Thread the parameters
    for node in self.children[1:-1]:
        lastNode = node.thread(lastNode)
    
    lastNode.addNext(self)
    
    # Thread the function body
    func_entry = AST.EntryNode()
        
    # Set the function definition in the global variable
    functions_def_non_threaded[functionNameNode.tok] = (func_entry, self)
    
    return self

@addToClass(AST.FunctionCallNode)
def thread(self, lastNode):
    functionName = self.children[0]
    
    lastNode.addNext(functionName)
    
    lastNode = functionName
    
    # Thread the parameters
    for node in self.children[1:]:
        lastNode = node.thread(lastNode)
        
    lastNode.addNext(self)
    
    func_name = self.children[0].tok
    
    if func_name not in functions_def_threaded:
        if func_name not in functions_def_non_threaded:
            raise Exception("Function " +  func_name + " not defined.")
        else:
            # Thread the function definition
            func_def_entry, function = functions_def_non_threaded[func_name]
            
            func_def_lastnode = function.children[-1].thread(func_def_entry)
            
            # Set the threaded function definition in the global variable
            functions_def_threaded[func_name] = (func_def_entry, func_def_lastnode)
    else:
        func_def_entry, func_def_lastnode = functions_def_threaded[func_name]
    
    self.addNext(func_def_entry)
            
    return func_def_lastnode

def setParentRec(node, parent):
    node.parent = parent
    for child in node.children:
        setParentRec(child, node)

def thread(tree):
    global entry
    entry = AST.EntryNode()
    
    setParentRec(tree, entry)
    
    tree.thread(entry)

    return entry


if __name__ == '__main__':
    from banger_parser import parse
    import sys
    import os

    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    entry = thread(ast)

    graph = ast.makegraphicaltree()
    entry.threadTree(graph)

    name = os.path.splitext(sys.argv[1])[0] + '-ast-threaded.pdf'
    graph.write_pdf(name)

    print(f"Wrote threaded ast to {name}")