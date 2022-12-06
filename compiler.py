import AST
from AST import addToClass


@addToClass(AST.Document)
def compile(self):
    html = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
'''

    for c in self.children:
        html += c.compile()

    html += '''
    </body>
</html>
'''

    return html


@addToClass(AST.ProgramBlock)
def compile(self):
    html = ""

    for c in self.children:
        html += c.compile()

    return html


@addToClass(AST.CodeBlock)
def compile(self):
    return "<pre><code>" + self.children[0].compile() + "</code></pre>"


@addToClass(AST.TitleBlock)
def compile(self):
    return "<h1>" + self.children[0].compile() + "</h1>"

@addToClass(AST.StringBlock)
def compile(self):
    html = str(self)
    return html

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
