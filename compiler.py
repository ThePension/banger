import AST
from AST import addToClass

# MathJax : https://github.com/mathjax/MathJax/


@addToClass(AST.Document)
def compile(self):
    html = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script type="text/x-mathjax-config">
            MathJax.Hub.Config({
                tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
            });
        </script>
        <script type="text/javascript" async
            src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
        </script>
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

@addToClass(AST.GenericBlock)
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

@addToClass(AST.ListBlock)
def compile(self):
    html = "<ul>"
    for c in self.children:
        html += c.compile()
    html += "</ul>"

    return html

@addToClass(AST.ListElement)
def compile(self):
    return "<li>" + self.children[0].compile() + "</li>"

@addToClass(AST.StringBlock)
def compile(self):
    html = r"" + str(self)[2:-3].replace('\\\\', '\\') # See https://stackoverflow.com/questions/11924706/how-to-get-rid-of-double-backslash-in-python-windows-file-path-string
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
