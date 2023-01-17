import re
import ply.lex as lex
from ply.lex import TOKEN
import sys

reserved_words = (
    "bg",
    "center",
    "right",
    "color",
    "left",
    "start",
    "stop",
    # "subpage",
    "toc",  # Table Of Contents
    "bulletpoint",
    "bv", # variable
)

tokens = (
    "NUMBER",
    "ERROR",
    "NEWLINE",
    "IGNORE",
    # "ADD_OP",
    # "MUL_OP",
    # "LPAREN",
    # "RPAREN",
    "EOL",
    "ASSIGNATION",
    "IDENTIFIER",
    # "LBRACKETS",
    # "RBRACKETS",
    "STRING",
    "COLOR_HEX",
    "BLOCK_ID",
) + tuple(map(lambda s: s.upper(), reserved_words))


t_BG = r"\bbg\b"
t_COLOR = r"\bcolor\b"
t_COLOR_HEX = r"[\#]{1}([0-9a-fA-F]{3}){1,2}"
t_CENTER = r"\bcenter\b"
t_RIGHT = r"\bright\b"
t_LEFT = r"\bleft\b"
# t_SUBPAGE = r"\bsubpage\b"
t_TOC = r"\btoc\b"
t_BULLETPOINT = r"\*[ ]"
t_START = r"\bstart\b"
t_STOP = r"\bstop\b"

title = r"\btitle\b"
list = r"\blist\b"
code = r"\bcode\b"
image = r"\bimage\b"
text = r"\btext\b"
t_BLOCK_ID = r'(' + title + r'|' + code + r'|' + list + r'|' + image + r'|' + text + r')'

t_ignore = r"[ ]"
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_UMINUS = r"\-"
# t_EOL = r'\;'
t_ASSIGNATION = r"(\s|^)->(\s|$)"
# t_LBRACKETS = r"\{"
# t_RBRACKETS = r"\}"

# string = r"(?!(title|list|code|image|text|{|}|" + r"|".join(reserved_words) + r"|" + t_COLOR_HEX + r")).+(\n)"

# Regex for lines that are not a block
# def t_STRING(t):
#     r"(?!(title|bv|list|code|image|text|bg|center|right|color|left|toc|start|stop|[\#]{1}([0-9a-fA-F]{3}){1,2})).+(\n)"
#     t.lexer.lineno += 1
    
    # t.value = t.value.replace("\n", "")
    
    return t

nondigit = r'([_A-Za-z])'
digit = r'([0-9])'
identifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'

t_BV = r"\bbv\b"

@TOKEN(identifier)
def t_IDENTIFIER(t):
    if t.value in reserved_words:
        t.type = t.value.upper()

    if t.value in ["title", "list", "code", "image", "text"]:
        t.type = "BLOCK_ID"
        
    return t


# def t_ADD_OP(t):
#     r"[\+-]"
#     return t

# def t_MUL_OP(t):
#     r"[\*\/]"
#     return t

# def t_NUMBER(t):
#     r"[+-]?([0-9]*[.])?[0-9]+"
#     t.value = float(t.value)
#     return t


def t_newline(t):
    r"\n"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex()

if __name__ == "__main__":
    prog = open(sys.argv[1]).read()

    lex.input(prog)

    while 1:
        tok = lex.token()

        if not tok:
            break
        print("line %d : %s (%s)" %
              (tok.lineno, tok.type, tok.value.replace("\n", "")))
