import ply.yacc as yacc
from banger_lex import tokens
import sys
import AST

operations = {
    "+" : lambda x, y : x + y,
    "-" : lambda x, y : x - y,
    "*" : lambda x, y : x * y,
    "/" : lambda x, y : x / y,
    "%" : lambda x, y : x % y,
}

def p_program(p):
    '''program : statement'''
    p[0] = AST.ProgramNode(p[1])

def p_statement_list(p):
    '''program : statement program'''
    p[0] = AST.ProgramNode([p[1]] + p[2].children)

def p_statement(p):
    '''statement : assignment
                 | print_statement
                 | if_statement
                 | while_statement
                 | for_statement
                 | function_definition
                 | function_call'''
    p[0] = p[1]

def p_if_statement(p):
    '''if_statement : IF expression LBRACE program RBRACE'''
    p[0] = AST.IfNode([p[2], p[4]])

def p_while_statement(p):
    '''while_statement : WHILE expression LBRACE program RBRACE'''
    p[0] = AST.WhileNode([p[2], p[4]])

def p_for_statement(p):
    '''for_statement : FOR LPAREN assignment SEMICOLON comparison SEMICOLON assignment RPAREN LBRACE program RBRACE'''
    # id = AST.TokenNode(p[2])
    # expr = p[4]
    # assign = AST.AssignNode([id, expr])
    print("for statement")
    p[0] = AST.ForNode([p[3], p[5], p[7]] + [p[10]])

def p_assignment(p):
    '''assignment : VARIABLE ASSIGN expression'''
    id = AST.TokenNode(p[1])
    expr = p[3]
    p[0] = AST.AssignNode([id, expr])

def p_function_definition(p):
    '''function_definition : FUNCTION VARIABLE LPAREN variable_list RPAREN LBRACE program RBRACE'''
    p[0] = AST.FunctionDefinitionNode([AST.TokenNode(p[2])] + p[4] + [p[7]])

def p_function_call(p):
    '''function_call : VARIABLE LPAREN argument_list RPAREN'''
    p[0] = AST.FunctionCallNode([AST.TokenNode(p[1])] + p[3])

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN'''
    p[0] = AST.PrintNode(p[3])

def p_expression_integer(p):
    '''expression : INTEGER'''    
    p[0] = AST.IntegerNode(p[1])
    
def p_expression_variable(p):
    '''expression : VARIABLE'''    
    p[0] = AST.TokenNode(p[1])

def p_expression_string(p):
    '''expression : STRING'''  
    p[0] = AST.StringNode(p[1])  

def p_expression_comparison(p):
    '''expression : comparison'''
    p[0] = p[1]

def p_expression_function_call(p):
    '''expression : function_call'''  
    p[0] = p[1]
    
def p_expr_op(p):
    '''expression : expression PLUS expression 
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MODULO expression'''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])
    
def p_expr_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_comparison(p):
    '''comparison : expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression'''
    p[0] = AST.ComparisonNode([AST.StringNode(p[2]), p[1], p[3]])

def p_variable_list(p):
    '''variable_list : VARIABLE
                     | variable_list COMMA VARIABLE'''
    if len(p) == 2:
        p[0] = [AST.TokenNode(p[1])]
    else:
        p[0] = p[1] + [AST.TokenNode(p[3])]
            
            
def p_argument_list(p):
    '''argument_list : expression
                     | argument_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_error(p):
    print(f"Syntax error at token {p.value}")


precedence = (
    ('left', 'LT'),
    ('left', 'LE'),
    ('left', 'GT'),
    ('left', 'GE'),
    ('left', 'EQ'),
    ('left', 'NE'),
    ('left', 'PLUS'),
    ('left', 'MINUS'),
    ('left', 'TIMES'),
    ('left', 'DIVIDE'),
    ('left', 'MODULO'),
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
    # [print(result) for result in results]
    print(results)
