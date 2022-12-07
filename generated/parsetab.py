
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGNATION BG BULLETPOINT CENTER CODE COLOR COLOR_HEX EOL ERROR IGNORE LBRACKETS LIST NEWLINE NUMBER RBRACKETS STRING SUBPAGE TITLE TOCdocument : blockblock : block_code\n             | block_title\n             | block_listblock : block_code block\n             | block_title block\n             | block_list blockblock_code : CODE LBRACKETS content RBRACKETSblock_list : LIST LBRACKETS list_elements RBRACKETSblock_list : LIST param LBRACKETS list_elements RBRACKETSlist_elements : list_elementlist_elements : list_element list_elementslist_element : BULLETPOINT contentblock_title : TITLE LBRACKETS content RBRACKETSblock_title : TITLE param LBRACKETS content RBRACKETSparam : param_bg\n             | param_fontparam : param_bg param\n             | param_font paramparam_bg : BG COLOR_HEXparam_font : COLOR COLOR_HEXcontent : STRING'
    
_lr_action_items = {'CODE':([0,3,4,5,33,34,36,40,41,],[6,6,6,6,-8,-14,-9,-15,-10,]),'TITLE':([0,3,4,5,33,34,36,40,41,],[7,7,7,7,-8,-14,-9,-15,-10,]),'LIST':([0,3,4,5,33,34,36,40,41,],[8,8,8,8,-8,-14,-9,-15,-10,]),'$end':([1,2,3,4,5,9,10,11,33,34,36,40,41,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-14,-9,-15,-10,]),'LBRACKETS':([6,7,8,14,15,16,20,25,26,27,28,],[12,13,19,24,-16,-17,32,-18,-19,-20,-21,]),'BG':([7,8,15,16,27,28,],[17,17,17,17,-20,-21,]),'COLOR':([7,8,15,16,27,28,],[18,18,18,18,-20,-21,]),'STRING':([12,13,24,31,],[22,22,22,22,]),'COLOR_HEX':([17,18,],[27,28,]),'BULLETPOINT':([19,22,30,32,38,],[31,-22,31,31,-13,]),'RBRACKETS':([21,22,23,29,30,35,37,38,39,],[33,-22,34,36,-11,40,-12,-13,41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'document':([0,],[1,]),'block':([0,3,4,5,],[2,9,10,11,]),'block_code':([0,3,4,5,],[3,3,3,3,]),'block_title':([0,3,4,5,],[4,4,4,4,]),'block_list':([0,3,4,5,],[5,5,5,5,]),'param':([7,8,15,16,],[14,20,25,26,]),'param_bg':([7,8,15,16,],[15,15,15,15,]),'param_font':([7,8,15,16,],[16,16,16,16,]),'content':([12,13,24,31,],[21,23,35,38,]),'list_elements':([19,30,32,],[29,37,39,]),'list_element':([19,30,32,],[30,30,30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> document","S'",1,None,None,None),
  ('document -> block','document',1,'p_document','banger_parser.py',7),
  ('block -> block_code','block',1,'p_block','banger_parser.py',11),
  ('block -> block_title','block',1,'p_block','banger_parser.py',12),
  ('block -> block_list','block',1,'p_block','banger_parser.py',13),
  ('block -> block_code block','block',2,'p_block_rec','banger_parser.py',17),
  ('block -> block_title block','block',2,'p_block_rec','banger_parser.py',18),
  ('block -> block_list block','block',2,'p_block_rec','banger_parser.py',19),
  ('block_code -> CODE LBRACKETS content RBRACKETS','block_code',4,'p_block_code','banger_parser.py',23),
  ('block_list -> LIST LBRACKETS list_elements RBRACKETS','block_list',4,'p_block_list','banger_parser.py',28),
  ('block_list -> LIST param LBRACKETS list_elements RBRACKETS','block_list',5,'p_block_list_with_param','banger_parser.py',32),
  ('list_elements -> list_element','list_elements',1,'p_list_elements','banger_parser.py',38),
  ('list_elements -> list_element list_elements','list_elements',2,'p_list_elements_rec','banger_parser.py',42),
  ('list_element -> BULLETPOINT content','list_element',2,'p_list_element','banger_parser.py',46),
  ('block_title -> TITLE LBRACKETS content RBRACKETS','block_title',4,'p_block_title','banger_parser.py',50),
  ('block_title -> TITLE param LBRACKETS content RBRACKETS','block_title',5,'p_block_title_with_param','banger_parser.py',54),
  ('param -> param_bg','param',1,'p_param','banger_parser.py',60),
  ('param -> param_font','param',1,'p_param','banger_parser.py',61),
  ('param -> param_bg param','param',2,'p_param_rec','banger_parser.py',65),
  ('param -> param_font param','param',2,'p_param_rec','banger_parser.py',66),
  ('param_bg -> BG COLOR_HEX','param_bg',2,'p_param_bg','banger_parser.py',70),
  ('param_font -> COLOR COLOR_HEX','param_font',2,'p_param_font','banger_parser.py',75),
  ('content -> STRING','content',1,'p_content','banger_parser.py',80),
]
