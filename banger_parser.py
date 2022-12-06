import ply.yacc as yacc
from banger_lex import tokens
import sys
import AST
import pydot
import os

# https://www.dabeaz.com/ply/ply.html#ply_nn4

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('right', 'UMINUS'),
)

# Définit un programme 'prog'


def p_prog(p):
    '''prog : statement'''
    p[0] = AST.ProgramNode(p[1])


def p_prog_rec(p):
    '''prog : statement EOE prog'''
    p[0] = AST.ProgramNode([p[1]] + p[3].children)


def p_statement_assign(p):
    '''statement : IDENTIFIER EQUALS expression'''
    id = AST.TokenNode(p[1])
    expression = p[3]
    p[0] = AST.AssignNode([id, expression])


def p_statement(p):
    '''statement : expression
                 | structure'''
    p[0] = p[1]


def p_statement_print(p):
    '''statement : PRINT expression'''
    p[0] = AST.PrintNode(p[2])


def p_struct_while(p):
    '''structure : WHILE expression LBRACKETS prog RBRACKETS'''
    cond = p[2]
    body = p[4]
    p[0] = AST.WhileNode([cond, body])


# Définit une expression avec opérateur


def p_expression_op(p):
    '''expression : expression ADD_OP expression
                  | expression MUL_OP expression'''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])


def p_expression_num(p):
    '''expression : NUMBER'''
    p[0] = AST.TokenNode(p[1])


def p_expression_paren(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]


def p_expression_uminus(p):
    '''expression : ADD_OP expression %prec UMINUS'''
    p[0] = AST.OpNode(p[1], [p[2]])


def p_expression_iden(p):
    '''expression : IDENTIFIER'''
    p[0] = AST.TokenNode(p[1])


def p_error(p):
    if p is not None:
        print(f"Syntax error in line {p.lineno} at {p.value} with {p.type}")
        parser = yacc.yacc()
        parser.errok()


precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('right', 'UMINUS'),          # Unary minus operator
)

yacc.yacc(outputdir="generated")


def parse(program):
    return yacc.parse(program)


if __name__ == "__main__":
    progs = open(sys.argv[1]).read()
    print(progs)
    result = yacc.parse(progs)
    print(f"Result = {result}")
    graph = result.makegraphicaltree()
    name = os.path.splitext(sys . argv[1])[0] + "−ast.pdf "
    graph.write_pdf(name)
    print("wrote ast to ", name)

    # for prog in progs:
    #     result = yacc.parse(prog)  # , debug=1
    #     print(result)
    #     print("____________________________________________________")
