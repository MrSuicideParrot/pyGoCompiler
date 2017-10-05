
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSINT FLOAT PLUS MINUS TIMES DIVIDE EQUALS LPAREN RPAREN ID BREAK CASE CHAN CONST CONTINUE DEFAULT DEFER ELSE FALLTHROUGH FOR FUNC GO GOTO IF IMPORT INTERFACE MAP PACKAGE RANGE RETURN SELECT STRUCT SWITCH TYPE VARstatement : ID EQUALS expressionstatement : expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : MINUS expression %prec UMINUSexpression : INTexpression : FLOATexpression : LPAREN expression RPARENexpression : ID'
    
_lr_action_items = {'ID':([0,4,7,8,9,10,11,12,],[2,14,14,14,14,14,14,14,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[4,-11,10,4,-8,-9,4,4,4,4,4,4,-7,-11,10,10,-3,-4,-5,-6,-10,]),'INT':([0,4,7,8,9,10,11,12,],[5,5,5,5,5,5,5,5,]),'FLOAT':([0,4,7,8,9,10,11,12,],[6,6,6,6,6,6,6,6,]),'LPAREN':([0,4,7,8,9,10,11,12,],[7,7,7,7,7,7,7,7,]),'$end':([1,2,3,5,6,13,14,16,17,18,19,20,21,],[0,-11,-2,-8,-9,-7,-11,-1,-3,-4,-5,-6,-10,]),'EQUALS':([2,],[8,]),'PLUS':([2,3,5,6,13,14,15,16,17,18,19,20,21,],[-11,9,-8,-9,-7,-11,9,9,-3,-4,-5,-6,-10,]),'TIMES':([2,3,5,6,13,14,15,16,17,18,19,20,21,],[-11,11,-8,-9,-7,-11,11,11,11,11,-5,-6,-10,]),'DIVIDE':([2,3,5,6,13,14,15,16,17,18,19,20,21,],[-11,12,-8,-9,-7,-11,12,12,12,12,-5,-6,-10,]),'RPAREN':([5,6,13,14,15,17,18,19,20,21,],[-8,-9,-7,-11,21,-3,-4,-5,-6,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,7,8,9,10,11,12,],[3,13,15,16,17,18,19,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> ID EQUALS expression','statement',3,'p_statement_assignment','plintax.py',15),
  ('statement -> expression','statement',1,'p_statement_expr','plintax.py',19),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','plintax.py',24),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','plintax.py',25),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','plintax.py',26),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','plintax.py',27),
  ('expression -> MINUS expression','expression',2,'p_expression_inverse','plintax.py',40),
  ('expression -> INT','expression',1,'p_expression_int','plintax.py',45),
  ('expression -> FLOAT','expression',1,'p_expression_float','plintax.py',50),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','plintax.py',55),
  ('expression -> ID','expression',1,'p_expression_var','plintax.py',60),
]
