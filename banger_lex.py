import ply.lex as lex
from ply.lex import TOKEN
import sys

reserved_words = (
    "bg",
    # "code",
    "center",
    "right",
    "left",
    # "list",
    # "subpage",
    # "title",
    "toc",  # Table Of Contents
    "bulletpoint",
    # "image",
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
    # "IDENTIFIER",
    "LBRACKETS",
    "RBRACKETS",
    "STRING",
    "COLOR",
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

title = r"\btitle\b"
list = r"\blist\b"
code = r"\bcode\b"
image = r"\bimage\b"
t_BLOCK_ID = r'(' + title + r'|' + list + r'|' + code + r'|' + image + r')'

t_ignore = r"[ ]"
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_UMINUS = r"\-"
t_EOL = r'\;'
t_ASSIGNATION = r'\='
t_LBRACKETS = r"\{"
t_RBRACKETS = r"\}"
t_STRING = r'".*?"'

nondigit = r'([_A-Za-z])'
digit = r'([0-9])'
identifier = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)'


# @ TOKEN(identifier)
# def t_IDENTIFIER(t):
#     if t.value in reserved_words:
#         t.type = t.value.upper()
#     return t

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
    r"\n+"
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
        print("line %d : %s (%s)" % (tok.lineno, tok.type, tok.value))
