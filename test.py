import ply.yacc as yacc
from banger_lex import tokens
import sys
import AST

def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : assignment
                 | print_statement
                 | if_statement'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : VARIABLE ASSIGN expression'''
    p[0] = ('assign', p[1], p[3])

def p_if_statement(p):
    '''if_statement : IF expression LBRACE statement_list RBRACE'''
    p[0] = ('if', p[2], p[4])


def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN'''
    p[0] = ('print', p[3])

def p_expression(p):
    '''expression : INTEGER
                  | VARIABLE
                  | STRING
                  | comparison'''
    p[0] = p[1]

def p_comparison(p):
    '''comparison : expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression'''
    p[0] = ('comp', p[2], p[1], p[3])

def p_error(p):
    print(f"Syntax error at token {p.value}")

            
# Build the parser
parser = yacc.yacc()

yacc.yacc(outputdir="generated")

def parse(program):
    return yacc.parse(program)


if __name__ == "__main__":
    import sys
    prog = open(sys.argv[1]).read()
    results = yacc.parse(prog, debug=0)
    [print(result) for result in results]
