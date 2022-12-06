import ply.yacc as yacc
from banger_lex import tokens
import sys
import AST
import pydot
import os


# Définit un programme 'prog'


def p_block(p):
    '''block : block
             | block_code
             | block_list
             | block_title
             | block_par'''
    p[0] = AST.Block(p[1])


def p_block_code(p):
    '''block_code : code LBRACKETS block RBRACKETS'''
    p[0] = AST.CodeBlock([p[1]] + p[3].children)


def p_block_list(p):
    '''block_list : list LBRACKETS block RBRACKETS'''
    p[0] = AST.ListBlock([p[1]] + p[3].children)


def p_list_element(p):
    '''list_element : list_element
                     | block'''
    p[0] = AST.ListElement([p[1]] + p[3].children)


def p_block_title(p):
    '''block_title : title LBRACKETS STRING RBRACKETS
                   | title LBRACKETS block RBRACKETS'''
    p[0] = AST.TitleBlock([p[1]] + p[3].children)


def p_param(p):
    '''param : param_bg
             | param_font'''
    p[0] = AST.ParamBlock([p[1]] + p[3].children)


def p_param_bg(p):
    '''param_bg : BG COLOR_TOK COLOR_HEX'''
    p[0] = AST.ParamBlock([p[1]] + p[3].children)


def p_param_font(p):
    '''param_font : param_font
                  | param_font param'''
    p[0] = AST.ParamBlock([p[1]] + p[3].children)


def p_token(p):
    '''token : STRING'''
    p[0] = AST.StringBlock([p[1]] + p[3].children)


def p_error(p):
    if p is not None:
        print(f"Syntax error in line {p.lineno} at {p.value} with {p.type}")
        parser = yacc.yacc()
        parser.errok()


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
