import ply.yacc as yacc
from banger_lex import tokens
import sys
import AST
import pydot
import os

def p_document(p):
    '''document : block'''
    p[0] = AST.Document(p[1])

def p_block(p):
    '''block : block_code
             | block_title'''
    p[0] = AST.ProgramBlock(p[1])


def p_block_code(p):
    '''block_code : CODE LBRACKETS STRING RBRACKETS'''
    p[0] = AST.CodeBlock(AST.StringBlock(p[3]))

def p_block_code_rec(p):
    '''block_code : CODE LBRACKETS STRING RBRACKETS block'''
    p[0] = AST.ProgramBlock([AST.CodeBlock(AST.StringBlock(p[3]))] + p[5].children)


# def p_block_list(p):
#     '''block_list : LIST LBRACKETS list_elements RBRACKETS
#                   | LIST LBRACKETS list_elements RBRACKETS block'''
#     p[0] = AST.ListBlock(p[3].children)


# def p_list_elements(p):
#     '''list_elements : list_element
#                      | list_element list_elements'''
#     p[0] = AST.ListElement(p[1])

# def p_list_element(p):
#     '''list_element : STRING'''
#     p[0] = AST.ListElement(p[1])


def p_block_title(p):
    '''block_title : TITLE LBRACKETS STRING RBRACKETS'''
    p[0] = AST.TitleBlock(AST.StringBlock(p[3]))

def p_block_title_rec(p):
    '''block_title : TITLE LBRACKETS STRING RBRACKETS block'''
    p[0] = AST.ProgramBlock([AST.TitleBlock(AST.StringBlock(p[3]))] + p[5].children)


# def p_param(p):
#     '''param : param_bg
#              | param_bg param'''
#     p[0] = AST.ParamBlock([p[1]] + p[3].children)


# def p_param_bg(p):
#     '''param_bg : BG COLOR_TOK
#                 | BG COLOR_HEX'''
#     p[0] = AST.ParamBlock([p[1]] + p[3].children)


# def p_param_font(p):
#     '''param_font : param_font
#                   | param_font param'''
#     p[0] = AST.ParamBlock([p[1]] + p[3].children)


def p_error(p):
    if p is not None:
        print(f"Syntax error in line {p.lineno} at {p.value} with {p.type}")
        parser = yacc.yacc()
        parser.errok()


yacc.yacc(outputdir="generated")


def parse(program):
    return yacc.parse(program)

if __name__ == "__main__":
    # progs = open(sys.argv[1]).read()
    # print(progs)
    # result = yacc.parse(progs)
    # print(f"Result = {result}")
    # graph = result.makegraphicaltree()
    # name = os.path.splitext(sys . argv[1])[0] + "−ast.pdf "
    # graph.write_pdf(name)
    # print("wrote ast to ", name)

    import sys
    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog, debug=0)
    print(result)
