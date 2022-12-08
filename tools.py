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