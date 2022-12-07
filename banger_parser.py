import ply.yacc as yacc
from banger_lex import tokens
import sys
import AST


def p_document(p):
    '''document : block'''
    p[0] = AST.Document(p[1])


def p_block(p):
    '''block : block_code
             | block_title
             | block_list
             | block_image'''
    p[0] = AST.GenericBlock(p[1])


def p_block_code(p):
    '''block_code : CODE LBRACKETS content RBRACKETS'''
    p[0] = AST.CodeBlock(p[3])


def p_block_code_rec(p):
    '''block_code : CODE LBRACKETS content RBRACKETS block'''
    p[0] = AST.GenericBlock([AST.CodeBlock(p[3])] + p[5].children)


def p_block_list(p):
    '''block_list : LIST LBRACKETS list_elements RBRACKETS'''
    p[0] = AST.ListBlock(p[3].children)


def p_block_list_rec(p):
    '''block_list : LIST LBRACKETS list_elements RBRACKETS block'''
    p[0] = AST.GenericBlock([AST.ListBlock(p[3].children)] + p[5].children)


def p_list_elements(p):
    '''list_elements : list_element'''
    p[0] = AST.ListElement(p[1])


def p_list_elements_rec(p):
    '''list_elements : list_element list_elements'''
    p[0] = AST.GenericBlock([p[1]] + p[2].children)


def p_list_element(p):
    '''list_element : BULLETPOINT content'''
    p[0] = AST.ListElement(p[2])


def p_block_title(p):
    '''block_title : TITLE LBRACKETS content RBRACKETS'''
    p[0] = AST.TitleBlock(p[3])


def p_block_title_rec(p):
    '''block_title : TITLE LBRACKETS content RBRACKETS block'''
    p[0] = AST.GenericBlock([AST.TitleBlock(p[3])] + p[5].children)


def p_block_title_with_param(p):
    '''block_title : TITLE param LBRACKETS content RBRACKETS'''
    titleBlock = AST.TitleBlock(p[3])
    titleBlock.params += [p[2]]
    p[0] = titleBlock


def p_block_title_with_param_rec(p):
    '''block_title : TITLE param LBRACKETS content RBRACKETS block'''
    titleBlock = AST.TitleBlock(p[4])
    titleBlock.params += [p[2]]
    p[0] = AST.GenericBlock([titleBlock] + [p[6]])


def p_block_image(p):
    '''block_image : IMAGE LBRACKETS content RBRACKETS block'''
    imageBlock = AST.ImageBlock(p[3])
    p[0] = AST.GenericBlock([imageBlock] + [p[5]])


def p_param(p):
    '''param : param_bg
             | param_font'''
    p[0] = AST.ParamBlock(p[1])


def p_param_rec(p):
    '''param : param_bg param
             | param_font param'''
    p[0] = AST.ParamBlock([p[1]] + p[2].children)


def p_param_bg(p):
    '''param_bg : BG COLOR_HEX'''
    p[0] = AST.ParamBGBlock(AST.StringBlock(p[2]))


def p_param_font(p):
    '''param_font : COLOR COLOR_HEX'''
    p[0] = AST.ParamFontBlock(AST.StringBlock(p[2]))


def p_content(p):
    '''content : STRING'''
    p[0] = AST.StringBlock(p[1])


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
