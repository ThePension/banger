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
                 | if_statement
                 | while_statement
                 | for_statement'''
                #  | function_definition
                #  | function_call'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : VARIABLE ASSIGN expression'''
    p[0] = ('assign', p[1], p[3])

def p_if_statement(p):
    '''if_statement : IF expression LBRACE statement_list RBRACE'''
    p[0] = ('if', p[2], p[4])

def p_while_statement(p):
    '''while_statement : WHILE expression LBRACE statement_list RBRACE'''
    p[0] = ('while', p[2], p[4])

def p_for_statement(p):
    '''for_statement : FOR VARIABLE IN INTEGER TO INTEGER LBRACE statement_list RBRACE'''
    p[0] = ('for', p[2], p[4], p[6], p[8])

# def p_function_definition(p):
#     '''function_definition : FUNCTION LPAREN variable_list RPAREN COLON statement_list'''
#     p[0] = ('function', p[3], p[6])

# def p_function_call(p):
#     '''function_call : VARIABLE LPAREN argument_list RPAREN'''
#     p[0] = ('call', p[1], p[3])

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN'''
    p[0] = ('print', p[3])

def p_expression(p):
    '''expression : INTEGER
                  | VARIABLE
                  | STRING
                  | comparison'''
                #   | function_call'''
    p[0] = p[1]

def p_comparison(p):
    '''comparison : expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression'''
    p[0] = ('comp', p[2], p[1], p[3])

# def p_variable_list(p):
#     '''variable_list : VARIABLE
#                      | variable_list COMMA VARIABLE'''
#     if len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         p[0] = p[1] + [p[3]]
            
            
# def p_argument_list(p):
#     '''argument_list : expression
#                      | argument_list COMMA expression'''
#     if len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         p[0] = p[1] + [p[3]]

def p_error(p):
    print(f"Syntax error at token {p.value}")


precedence = (
    ('left', 'LT'),
    ('left', 'LE'),
    ('left', 'GT'),
    ('left', 'GE'),
    ('left', 'EQ'),
    ('left', 'NE'),
)
            
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
