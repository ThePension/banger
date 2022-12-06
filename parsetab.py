
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGNATION BG BULLETPOINT CENTER CODE COLOR_HEX COLOR_TOK EOL ERROR IDENTIFIER IGNORE LBRACKETS LIST NEWLINE NUMBER RBRACKETS STRING SUBPAGE TITLE TOCdocument : blockblock : block_code\n             | block_title\n             | block_listblock_code : CODE LBRACKETS STRING RBRACKETSblock_code : CODE LBRACKETS STRING RBRACKETS blockblock_list : LIST LBRACKETS list_elements RBRACKETSblock_list : LIST LBRACKETS list_elements RBRACKETS blocklist_elements : list_elementlist_elements : list_element list_elementslist_element : STRINGblock_title : TITLE LBRACKETS STRING RBRACKETSblock_title : TITLE LBRACKETS STRING RBRACKETS block'
    
_lr_action_items = {'CODE':([0,17,18,19,],[6,6,6,6,]),'TITLE':([0,17,18,19,],[7,7,7,7,]),'LIST':([0,17,18,19,],[8,8,8,8,]),'$end':([1,2,3,4,5,17,18,19,21,22,23,],[0,-1,-2,-3,-4,-5,-12,-7,-6,-13,-8,]),'LBRACKETS':([6,7,8,],[9,10,11,]),'STRING':([9,10,11,15,16,],[12,13,16,16,-11,]),'RBRACKETS':([12,13,14,15,16,20,],[17,18,19,-9,-11,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'document':([0,],[1,]),'block':([0,17,18,19,],[2,21,22,23,]),'block_code':([0,17,18,19,],[3,3,3,3,]),'block_title':([0,17,18,19,],[4,4,4,4,]),'block_list':([0,17,18,19,],[5,5,5,5,]),'list_elements':([11,15,],[14,20,]),'list_element':([11,15,],[15,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> document","S'",1,None,None,None),
  ('document -> block','document',1,'p_document','banger_parser.py',9),
  ('block -> block_code','block',1,'p_block','banger_parser.py',13),
  ('block -> block_title','block',1,'p_block','banger_parser.py',14),
  ('block -> block_list','block',1,'p_block','banger_parser.py',15),
  ('block_code -> CODE LBRACKETS STRING RBRACKETS','block_code',4,'p_block_code','banger_parser.py',20),
  ('block_code -> CODE LBRACKETS STRING RBRACKETS block','block_code',5,'p_block_code_rec','banger_parser.py',24),
  ('block_list -> LIST LBRACKETS list_elements RBRACKETS','block_list',4,'p_block_list','banger_parser.py',29),
  ('block_list -> LIST LBRACKETS list_elements RBRACKETS block','block_list',5,'p_block_list_rec','banger_parser.py',33),
  ('list_elements -> list_element','list_elements',1,'p_list_elements','banger_parser.py',38),
  ('list_elements -> list_element list_elements','list_elements',2,'p_list_elements_rec','banger_parser.py',42),
  ('list_element -> STRING','list_element',1,'p_list_element','banger_parser.py',46),
  ('block_title -> TITLE LBRACKETS STRING RBRACKETS','block_title',4,'p_block_title','banger_parser.py',51),
  ('block_title -> TITLE LBRACKETS STRING RBRACKETS block','block_title',5,'p_block_title_rec','banger_parser.py',55),
]
