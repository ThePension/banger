import textwrap

def remove_superflu_tabs(s):
    # Split by \\n
    lines = s.split("\\n")

    # If every line starts with 4 spaces, remove them
    for line in lines:
        # If the line doesn't start with 4 spaces or a tab
        if not (line[:4] == "    " or line[:1] == "\\t") and line != "":
            return "<br />".join(lines)
        
    # Remove the first 4 spaces of each line
    for i in range(len(lines)):
        lines[i] = lines[i][4:]

    # Join the lines with a <br> tag between each line
    s = "\\n".join(lines)

    # Recursive call in case every line starts with 4 spaces one more time
    s = remove_superflu_tabs(s)

    return "<br />".join(s.split("\\n"))

# def auto_indent(code):
#     # Split the code by \\n
#     lines = code.split("<br>")

#     # Get the indentation of the first line
#     indent = 0
#     for char in lines[0]:
#         if char == " ":
#             indent += 1
#         else:
#             break

#     # Remove the indentation of the first line
#     lines[0] = lines[0][indent:]

#     # Add the indentation to each line
#     for i in range(len(lines)):
#         lines[i] = "&nbsp; " * indent + lines[i]

#     # Join the lines with a \\n between each line
#     return "<br>".join(lines)

def auto_indent(code: str) -> str:
    # return textwrap.indent(code.replace("<br>", "\n"), '&nbsp; ')
    # Split by \\n
    lines = code.split("\\n")

    # If every line starts with 4 spaces, remove them
    for line in lines:
        # If the line doesn't start with 4 spaces or a tab
        if not (line[:4] == "    " or line[:1] == "\\t") and line != "":
            return "<br />".join(lines)
        
    # Remove the first 4 spaces of each line
    for i in range(len(lines)):
        lines[i] = lines[i][4:]

    # Join the lines with a <br> tag between each line
    s = "\\n".join(lines)

    # Recursive call in case every line starts with 4 spaces one more time
    s = remove_superflu_tabs(s)

    return "<br />".join(s.split("\\n"))

if __name__ == "__main__":
    code = """
        function(window) {

            function myService() {
                var self = this;

                this.hello = world

                this.printHello = function() {
                    console.log('from this: hello', self.hello)
                }
            }
        }
    """
    
    print(auto_indent(code))