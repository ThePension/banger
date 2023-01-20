import AST
from AST import addToClass
from functools import reduce

# operations = {
#     "+" : lambda x , y : x + y,
#     "-" : lambda x , y : x - y,
#     "*" : lambda x , y : x * y,
#     "/" : lambda x , y : x / y,
# }

comparison_ops = {
    "<" : lambda x , y : x < y,
    ">" : lambda x , y : x > y,
    "<=" : lambda x , y : x <= y,
    ">=" : lambda x , y : x >= y,
    "==" : lambda x , y : x == y,
    "!=" : lambda x , y : x != y,
}

vars = { }

@addToClass(AST.ProgramNode)
def execute(self):
    for c in self.children:
        c.execute()

@addToClass(AST.TokenNode)
def execute(self):
    if isinstance(self.tok, str):
        try:
            return vars[self.tok]
        except KeyError:
            print("*** Error : variable %s undefined !" % self.tok)
    return self.tok

# @addToClass(AST.OpNode)
# def execute(self):
#     args = [c.execute() for c in self.children]
#     if len(args) == 1:
#         args.insert(0, 0)
#     return reduce(operations[self.op], args)

@addToClass(AST.AssignNode)
def execute(self):
    vars[self.children[0].tok] = self.children[1].execute()

@addToClass(AST.PrintNode)
def execute(self):
    print(self.children[0].execute())

@addToClass(AST.ComparisonNode)
def execute(self):
    args = [c.execute() for c in self.children]
    return comparison_ops[args[0]](args[1], args[2])

@addToClass(AST.WhileNode)
def execute(self):
    while(self.children[0].execute()):
        self.children[1].execute()

@addToClass(AST.IfNode)
def execute(self):
    if(self.children[0].execute()):
        self.children[1].execute()
    # else statement (not implemented yet)
    # else:
    #     self.children[2].execute()

@addToClass(AST.ForNode)
def execute(self):
    vars[self.children[0].children[0].tok] = self.children[0].children[1].execute()
    while(self.children[1].execute()):
        self.children[2].execute()
        vars[self.children[0].children[0].tok] += 1

@addToClass(AST.IntegerNode)
def execute(self):
    return self.tok

@addToClass(AST.StringNode)
def execute(self):
    return self.tok

if __name__ == "__main__" :
    from banger_parser import parse
    import sys
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    ast.execute()