import ply.yacc as yacc
from banger_lex import tokens
import sys
import AST

# Variable assignments
def p_assignment(p):
    '''statement : VARIABLE ASSIGN expression'''
    p[0] = ('assign', p[1], p[3])

# If statements
def p_if(p):
    '''statement : IF LPAREN expression RPAREN LBRACE statements RBRACE
                 | IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE'''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
    else:
        p[0] = ('if-else', p[3], p[6], p[10])

# While loops
def p_while(p):
    '''statement : WHILE LPAREN expression RPAREN LBRACE statements RBRACE'''
    p[0] = ('while', p[3], p[6])

# For loops  
def p_for_loop(p):
    '''statement : FOR VARIABLE IN VARIABLE LBRACE statements RBRACE'''
    p[0] = ("for_loop", p[2], p[4], p[6])

# Print statement
def p_print(p):
    '''statement : PRINT LPAREN expression RPAREN'''
    p[0] = ('print', p[3])
    
# Function definition
def p_function(p):
    '''statement : FUNCTION VARIABLE LPAREN parameters RPAREN LBRACE statements RBRACE'''
    p[0] = ('function', p[2], p[4], p[7])

def p_parameters(p):
    '''parameters : VARIABLE
                  | parameters COMMA VARIABLE'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# Expressions
def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression
                  | expression AND expression
                  | expression OR expression
                  | NOT expression
                  | LPAREN expression RPAREN
                  | INTEGER
                  | VARIABLE
                  | STRING'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    elif len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

# Statements
def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_error(p):
    print(f"Syntax error at token {p.value}")

yacc.yacc(outputdir="generated")


def parse(program):
    return yacc.parse(program)


if __name__ == "__main__":
    import sys
    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog, debug=0)
    print(result)
