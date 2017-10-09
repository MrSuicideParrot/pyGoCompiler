
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSINT FLOAT PLUS MINUS TIMES DIVIDE EQUALS LPAREN RPAREN ID COMMENT STRING EQUALSTO MORE LESS MOREEQUAL LESSEQUAL NOTEQUAL BREAK CASE CHAN CONST CONTINUE DEFAULT DEFER ELSE FALLTHROUGH FOR FUNC GO GOTO IF IMPORT INTERFACE MAP PACKAGE RANGE RETURN SELECT STRUCT SWITCH TYPE VARstatement : expr_listexpr_list : expression\n                 | expression expr_listexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : MINUS expression %prec UMINUSexpression : INTexpression : FLOATexpression : ID'
    
_lr_action_items = {'MINUS':([0,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,],[4,10,4,-9,-10,-11,4,4,4,4,-8,-4,-5,-6,-7,4,-5,]),'INT':([0,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,],[5,5,5,-9,-10,-11,5,5,5,5,-8,-4,-5,-6,-7,5,-5,]),'FLOAT':([0,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,],[6,6,6,-9,-10,-11,6,6,6,6,-8,-4,-5,-6,-7,6,-5,]),'ID':([0,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,],[7,7,7,-9,-10,-11,7,7,7,7,-8,-4,-5,-6,-7,7,-5,]),'$end':([1,2,3,5,6,7,8,13,14,15,16,17,19,],[0,-1,-2,-9,-10,-11,-3,-8,-4,-5,-6,-7,-5,]),'PLUS':([3,5,6,7,13,14,15,16,17,19,],[9,-9,-10,-11,-8,-4,-5,-6,-7,-5,]),'TIMES':([3,5,6,7,13,14,15,16,17,19,],[11,-9,-10,-11,-8,11,11,-6,-7,11,]),'DIVIDE':([3,5,6,7,13,14,15,16,17,19,],[12,-9,-10,-11,-8,12,12,-6,-7,12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expr_list':([0,3,],[2,8,]),'expression':([0,3,4,9,10,11,12,18,],[3,3,13,14,15,16,17,19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expr_list','statement',1,'p_statement_expr','plintax.py',25),
  ('expr_list -> expression','expr_list',1,'p_expr_list','plintax.py',30),
  ('expr_list -> expression expr_list','expr_list',2,'p_expr_list','plintax.py',31),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','plintax.py',40),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','plintax.py',41),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','plintax.py',42),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','plintax.py',43),
  ('expression -> MINUS expression','expression',2,'p_expression_inverse','plintax.py',56),
  ('expression -> INT','expression',1,'p_expression_int','plintax.py',61),
  ('expression -> FLOAT','expression',1,'p_expression_float','plintax.py',66),
  ('expression -> ID','expression',1,'p_expression_var','plintax.py',76),
]
