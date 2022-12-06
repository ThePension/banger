import AST
from AST import addToClass


@addToClass(AST.Block)
def compile(self):
    bytecode = ""
    for c in self.children:
        bytecode += c.compile()

    return bytecode


@addToClass(AST.CodeBlock)
def compile(self):
    bytecode = ""
    return bytecode


@addToClass(AST.ListBlock)
def compile(self):
    bytecode = ""

    args = [c.compile() for c in self.children]

    for arg in args:
        bytecode += arg

    return bytecode


@addToClass(AST.TitleBlock)
def compile(self):
    bytecode = self.children[1].compile()
    return bytecode


@addToClass(AST.ListBlock)
def compile(self):
    bytecode = self.children[0].compile()
    return bytecode


@addToClass(AST.ParamBlock)
def compile(self):
    bytecode = ""
    return bytecode


if __name__ == "__main__":
    from banger_parser import parse
    import sys
    import os

    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    compiled = ast.compile()
    name = os.path.splitext(sys.argv[1])[0] + ".html"
    outfile = open(name, "w")
    outfile.write(compiled)
    outfile.close()
    print("Wrote output to ", name)
