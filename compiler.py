import AST
from AST import addToClass
from tools import remove_superflu_tabs

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
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
        <title>Document</title>
        <style>
            pre {
                background: #f4f4f4;
                border: 1px solid #ddd;
                border-left: 3px solid #f36d33;
                color: #666;
                page-break-inside: avoid;
                font-family: monospace;
                font-size: 15px;
                line-height: 1.6;
                margin-bottom: 1.6em;
                max-width: 100%;
                overflow: auto;
                padding: 1em 1.5em;
                display: block;
                word-wrap: break-word;
                margin: 1em 1.5em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="row">
'''

    for c in self.children:
        html += c.compile()

    html += '''
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
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
    html =  "<pre "

    for p in self.params:
        html += p.compile()
    
    html += "><code>" + remove_superflu_tabs(self.children[0].compile()) + "</code></pre>"

    return html


@addToClass(AST.TitleBlock)
def compile(self):
    html = "<h1 "

    for p in self.params:
        html += p.compile()

    html += ">"
    html += self.children[0].compile() + "</h1>"

    return html


@addToClass(AST.ListBlock)
def compile(self):
    html = "<ul "
    
    for p in self.params:
        html += p.compile()

    html += " class='list-group list-group-flush'>"

    for c in self.children:
        html += c.compile()

    html += "</ul>"

    return html


@addToClass(AST.ListElement)
def compile(self):
    return "<li class='list-group-item'>" + self.children[0].compile() + "</li>"


@addToClass(AST.ImageBlock)
def compile(self):
    html = "<img src=\"" + self.children[0].compile() + "\" "

    for p in self.params:
        html += p.compile()

    html += " >"
    return html

@addToClass(AST.TextBlock)
def compile(self):
    html = "<p>" + self.children[0].compile() + "</p>"
    return html

@addToClass(AST.StringBlock)
def compile(self):
    # See https://stackoverflow.com/questions/11924706/how-to-get-rid-of-double-backslash-in-python-windows-file-path-string
    html = r"" + str(self)[2:-3].replace('\\\\', '\\').replace("\\n", "<br>")
    return html


@addToClass(AST.ParamBlock)
def compile(self):
    html = "style=\""

    for c in self.children:
        html += c.compile()

    html += "\""
    return html


@addToClass(AST.ParamBGBlock)
def compile(self):
    return "background-color: " + str(self)[1:-2].replace('\\\\', '\\') + ";"


@addToClass(AST.ParamFontBlock)
def compile(self):
    return "color: " + str(self)[1:-2].replace('\\\\', '\\') + ";"

@addToClass(AST.ParamAlignCenterBlock)
def compile(self):
    return "text-align: center;" # "margin: 0 auto; text-align: center;"

@addToClass(AST.ParamAlignRightBlock)
def compile(self):
    return "text-align: right;"

@addToClass(AST.ParamAlignLeftBlock)
def compile(self):
    return "text-align: left;"


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
