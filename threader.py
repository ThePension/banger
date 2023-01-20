import AST
from AST import ProgramNode, addToClass


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

def thread(tree):
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