import ply.yacc as yacc
from banger_lex import tokens
import sys
import AST


def p_document(p):
    '''document : block_light'''
    p[0] = AST.Document(p[1])

def p_block_light(p):
    '''block_light : block_complete'''
    p[0] = p[1]

def p_block_light_rec(p):
    '''block_light : block_complete block_light'''
    p[0] = AST.GenericBlock([p[1]] + [p[2]])

def p_block(p):
    '''block_complete : block_id LBRACKETS block_content RBRACKETS'''
    p[1].children += [p[3]]
    p[0] = p[1]

def p_block_with_param(p):
    '''block_complete : block_id param LBRACKETS block_content RBRACKETS'''
    p[1].children += [p[4]]
    p[1].params += [p[2]]
    p[0] = p[1]

def p_block_id_code(p):
    '''block_id : BLOCK_ID'''
    block_id = p[1]

    if block_id.upper() == "CODE":
        p[0] = AST.CodeBlock()
    elif block_id.upper() == "LIST":
        p[0] = AST.ListBlock()
    elif block_id.upper() == "TITLE":
        p[0] = AST.TitleBlock()
    elif block_id.upper() == "IMAGE":
        p[0] = AST.ImageBlock()
    elif block_id.upper() == "TEXT":
        p[0] = AST.TextBlock()
            

def p_block_content(p):
    '''block_content : block_light
                     | list_elements
                     | content_string'''
    p[0] = p[1]

def p_list_elements(p):
    '''list_elements : list_element'''
    p[0] = AST.ListElement(p[1])


def p_list_elements_rec(p):
    '''list_elements : list_element list_elements'''
    p[0] = AST.GenericBlock([p[1]] + p[2].children)


def p_list_element(p):
    '''list_element : BULLETPOINT content_string'''
    p[0] = AST.ListElement(p[2])

def p_param(p):
    '''param : param_bg
             | param_font
             | param_align'''
    p[0] = AST.ParamBlock(p[1])

def p_param_rec(p):
    '''param : param_bg param
             | param_font param
             | param_align param'''
    p[0] = AST.ParamBlock([p[1]] + p[2].children)

def p_param_bg(p):
    '''param_bg : BG COLOR_HEX'''
    p[0] = AST.ParamBGBlock(AST.StringBlock(p[2]))
    
def p_param_font(p):
    '''param_font : COLOR COLOR_HEX'''
    p[0] = AST.ParamFontBlock(AST.StringBlock(p[2]))

def p_param_align_center(p):
    '''param_align : CENTER'''
    p[0] = AST.ParamAlignCenterBlock()

def p_param_align_right(p):
    '''param_align : RIGHT'''
    p[0] = AST.ParamAlignRightBlock()

def p_param_align_left(p):
    '''param_align : LEFT'''
    p[0] = AST.ParamAlignLeftBlock()
    
def p_content(p):
    '''content_string : STRING'''
    print(p)
    p[0] = AST.StringBlock(str(p[1]))


def p_error(p):
    if p is not None:
        print(f"Syntax error in line {p.lineno} at {p.value} with {p.type}")
        print(p)
        parser = yacc.yacc()
        parser.errok()


yacc.yacc(outputdir="generated")


def parse(program):
    return yacc.parse(program)


if __name__ == "__main__":
    import sys
    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog, debug=0)
    print(result)
