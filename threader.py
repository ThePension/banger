import AST
from AST import ProgramNode, addToClass

entry = None

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
    
    # From the if, go through the program to get the last node (should be programNode)
    lastNode = self.children[1].thread(self) # lastNode == programNode
    
    # Program is done
    # From the program return to the condition (which is the last "next node" of the node before the condition)
    lastNode.addNext(self)
    
    return self

@addToClass(AST.ForNode)
def thread(self, lastNode):
    beforeAssign = lastNode
    assignNode = self.children[0]
    
    # Go through the assignation to get the last node
    lastNode = assignNode.thread(lastNode)
    
    toNode = self.children[1]
    
    lastNode.addNext(toNode)
    
    # From the last node of the assignation, go to the for (testing condition), instead of program
    toNode.addNext(self)
    
    lastNode = self.children[2].thread(self)
    
    lastNode.addNext(beforeAssign.next[-1])
    
    return self

@addToClass(AST.FunctionDefinitionNode)
def thread(self, lastNode):
    lastNode.addNext(self)
    lastNode = self.children[0].thread(self)
    
    for node in self.children[1:-1]:
        lastNode = node.thread(lastNode)
        
    lastNode.addNext(self)
    # self.next[-1].addNext(self.children[-1])
    return self

@addToClass(AST.FunctionCallNode)
def thread(self, lastNode):
    lastNode.addNext(self)
    func_def = None
    # Search for the function definition in the previous nodes
    for node in entry.next:
        if isinstance(node, AST.FunctionDefinitionNode) and node.children[0].tok == self.children[0].tok:
            func_def = node
            break
    if not func_def:
        raise Exception("Function not defined.")
    
    lastNode = func_def.children[-1].thread(self)
    
    lastNode.addNext(self)
    
    return self


# @addToClass(AST.FunctionCallNode)
# def thread(self, lastNode):
#     # Get the function definition node
#     function = self.children[0]
#     # Add a link from the last node to the function definition node
#     lastNode.addNext(function)
#     # The function call node is the exit point for the function
#     return self



def thread(tree):
    global entry
    entry = AST.EntryNode()
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