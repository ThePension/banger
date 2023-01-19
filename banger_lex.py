import re
import ply.lex as lex
from ply.lex import TOKEN
import sys

tokens = [
    'VARIABLE',
    'ASSIGN',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'PRINT',
    'FUNCTION',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'INTEGER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LT',
    'LE',
    'GT',
    'GE',
    'EQ',
    'NE',
    'AND',
    'OR',
    'NOT',
    'COLON',
    'IN',
    'TO',
]

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'print': 'PRINT',
    'function': 'FUNCTION',
    'in': 'IN',
    'to': 'TO',
    # 'function_call': 'FUNCTION_CALL'
}

t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_COLON = r':'
t_IN = r'in'
t_TO = r'to'

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"(?:\\\"|[^"])*\"'
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'\#.*'
    pass

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lex.lex()

if __name__ == "__main__":
    prog = open(sys.argv[1]).read()
    print(sys.argv[1])
    lex.input(prog)

    while 1:
        tok = lex.token()

        if not tok:
            break
        print("line %d : %s (%s)" %
              (tok.lineno, tok.type, tok.value))
