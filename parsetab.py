
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLESSMOREEQUALSTOMOREEQUALLESSEQUALNOTEQUALleftPLUSMINUSleftTIMESDIVIDEINT FLOAT PLUS MINUS TIMES DIVIDE EQUALS LPAREN RPAREN LCURLBRACKET RCURLBRACKET ID COMMENT STRING ASSIGN SEMICOLON COMMA POINT EQUALSTO MORE LESS MOREEQUAL LESSEQUAL NOTEQUAL BREAK CASE CHAN CONST CONTINUE DEFAULT DEFER ELSE FALLTHROUGH FOR FUNC GO GOTO IF IMPORT INTERFACE MAP PACKAGE RANGE RETURN SELECT STRUCT SWITCH TYPE VAR MAIN FMT PRINT SCAN TRUE FALSEstatement : PACKAGE MAIN IMPORT STRING FUNC MAIN LPAREN RPAREN LCURLBRACKET list RCURLBRACKET\n                 | PACKAGE MAIN IMPORT STRING FUNC MAIN LPAREN RPAREN LCURLBRACKET RCURLBRACKETlist : inst\n            | inst listassignment : ID ASSIGN expressionAR\n                  | ID ASSIGN expressionBoinst : FOR expressionBo LCURLBRACKET list RCURLBRACKET\n            | FOR assignment SEMICOLON expressionBo SEMICOLON expressionAR LCURLBRACKET list RCURLBRACKETinst : assignment SEMICOLONinst : IF expressionBo LCURLBRACKET list RCURLBRACKET ELSE LCURLBRACKET list RCURLBRACKET\n            | IF expressionBo LCURLBRACKET list RCURLBRACKETlistID : expressionAR\n              | expressionBo\n              | expressionBo COMMA listID\n              | expressionAR COMMA listIDinst : FMT POINT PRINT LPAREN listID RPAREN SEMICOLON\n            | FMT POINT SCAN LPAREN listID RPAREN SEMICOLONexpressionAR : expressionAR PLUS expressionAR\n                     | expressionAR MINUS expressionAR\n                     | expressionAR TIMES expressionAR\n                     | expressionAR DIVIDE expressionARexpressionAR : INTexpressionAR : FLOATexpressionAR : LPAREN expressionAR RPARENexpressionBo : expressionAR MORE expressionAR\n                    | expressionAR LESS expressionAR\n                    | expressionAR MOREEQUAL expressionAR\n                    | expressionAR LESSEQUAL expressionAR\n                    | expressionBo NOTEQUAL expressionBo\n                    | expressionAR NOTEQUAL expressionAR\n                    | expressionBo EQUALSTO expressionBo\n                    | expressionAR EQUALSTO expressionAR\n                    | IDexpressionBo : TRUE\n                    | FALSEexpressionBo : LPAREN expressionBo RPAREN'
    
_lr_action_items = {'PACKAGE':([0,],[2,]),'$end':([1,12,19,],[0,-2,-1,]),'MAIN':([2,6,],[3,7,]),'IMPORT':([3,],[4,]),'STRING':([4,],[5,]),'FUNC':([5,],[6,]),'LPAREN':([7,14,16,27,34,36,37,38,39,40,41,42,43,44,45,46,47,48,52,53,56,62,75,76,79,89,90,],[8,27,27,27,56,27,27,27,62,62,62,62,62,62,62,62,62,62,75,76,56,62,56,56,62,56,56,]),'RPAREN':([8,25,26,28,29,32,49,50,58,59,61,63,64,65,66,67,68,69,70,71,72,73,77,80,82,83,84,85,95,96,],[9,-34,-35,-22,-23,-33,72,73,-29,-31,-25,-26,-27,-28,-30,-32,-18,-19,-20,-21,-36,-24,73,73,88,-12,-13,91,-15,-14,]),'LCURLBRACKET':([9,21,24,25,26,28,29,31,32,58,59,61,63,64,65,66,67,68,69,70,71,72,73,86,87,],[10,35,-33,-34,-35,-22,-23,51,-33,-29,-31,-25,-26,-27,-28,-30,-32,-18,-19,-20,-21,-36,-24,92,93,]),'RCURLBRACKET':([10,11,13,20,30,57,74,78,81,94,97,98,99,100,101,],[12,19,-3,-4,-9,78,81,-7,-11,-16,-17,100,101,-8,-10,]),'FOR':([10,13,30,35,51,78,81,92,93,94,97,100,101,],[14,14,-9,14,14,-7,-11,14,14,-16,-17,-8,-10,]),'IF':([10,13,30,35,51,78,81,92,93,94,97,100,101,],[16,16,-9,16,16,-7,-11,16,16,-16,-17,-8,-10,]),'FMT':([10,13,30,35,51,78,81,92,93,94,97,100,101,],[17,17,-9,17,17,-7,-11,17,17,-16,-17,-8,-10,]),'ID':([10,13,14,16,27,30,34,35,36,37,38,51,56,75,76,78,81,89,90,92,93,94,97,100,101,],[18,18,24,32,32,-9,32,18,32,32,32,18,32,32,32,-7,-11,32,32,18,18,-16,-17,-8,-10,]),'TRUE':([14,16,27,34,36,37,38,56,75,76,89,90,],[25,25,25,25,25,25,25,25,25,25,25,25,]),'FALSE':([14,16,27,34,36,37,38,56,75,76,89,90,],[26,26,26,26,26,26,26,26,26,26,26,26,]),'INT':([14,16,27,34,36,37,38,39,40,41,42,43,44,45,46,47,48,56,62,75,76,79,89,90,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'FLOAT':([14,16,27,34,36,37,38,39,40,41,42,43,44,45,46,47,48,56,62,75,76,79,89,90,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'SEMICOLON':([15,22,25,26,28,29,32,54,55,58,59,60,61,63,64,65,66,67,68,69,70,71,72,73,88,91,],[30,38,-34,-35,-22,-23,-33,-5,-6,-29,-31,79,-25,-26,-27,-28,-30,-32,-18,-19,-20,-21,-36,-24,94,97,]),'POINT':([17,],[33,]),'ASSIGN':([18,24,],[34,34,]),'NOTEQUAL':([21,23,24,25,26,28,29,31,32,49,50,54,55,58,59,60,61,63,64,65,66,67,68,69,70,71,72,73,77,83,84,],[36,43,-33,-34,-35,-22,-23,36,-33,36,43,43,36,None,None,36,-25,-26,-27,-28,-30,-32,-18,-19,-20,-21,-36,-24,43,43,36,]),'EQUALSTO':([21,23,24,25,26,28,29,31,32,49,50,54,55,58,59,60,61,63,64,65,66,67,68,69,70,71,72,73,77,83,84,],[37,44,-33,-34,-35,-22,-23,37,-33,37,44,44,37,None,None,37,-25,-26,-27,-28,-30,-32,-18,-19,-20,-21,-36,-24,44,44,37,]),'MORE':([23,28,29,50,54,68,69,70,71,73,77,83,],[39,-22,-23,39,39,-18,-19,-20,-21,-24,39,39,]),'LESS':([23,28,29,50,54,68,69,70,71,73,77,83,],[40,-22,-23,40,40,-18,-19,-20,-21,-24,40,40,]),'MOREEQUAL':([23,28,29,50,54,68,69,70,71,73,77,83,],[41,-22,-23,41,41,-18,-19,-20,-21,-24,41,41,]),'LESSEQUAL':([23,28,29,50,54,68,69,70,71,73,77,83,],[42,-22,-23,42,42,-18,-19,-20,-21,-24,42,42,]),'PLUS':([23,28,29,50,54,61,63,64,65,66,67,68,69,70,71,73,77,80,83,86,],[45,-22,-23,45,45,45,45,45,45,45,45,-18,-19,-20,-21,-24,45,45,45,45,]),'MINUS':([23,28,29,50,54,61,63,64,65,66,67,68,69,70,71,73,77,80,83,86,],[46,-22,-23,46,46,46,46,46,46,46,46,-18,-19,-20,-21,-24,46,46,46,46,]),'TIMES':([23,28,29,50,54,61,63,64,65,66,67,68,69,70,71,73,77,80,83,86,],[47,-22,-23,47,47,47,47,47,47,47,47,47,47,-20,-21,-24,47,47,47,47,]),'DIVIDE':([23,28,29,50,54,61,63,64,65,66,67,68,69,70,71,73,77,80,83,86,],[48,-22,-23,48,48,48,48,48,48,48,48,48,48,-20,-21,-24,48,48,48,48,]),'COMMA':([25,26,28,29,32,58,59,61,63,64,65,66,67,68,69,70,71,72,73,83,84,],[-34,-35,-22,-23,-33,-29,-31,-25,-26,-27,-28,-30,-32,-18,-19,-20,-21,-36,-24,89,90,]),'PRINT':([33,],[52,]),'SCAN':([33,],[53,]),'ELSE':([81,],[87,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'list':([10,13,35,51,92,93,],[11,20,57,74,98,99,]),'inst':([10,13,35,51,92,93,],[13,13,13,13,13,13,]),'assignment':([10,13,14,35,51,92,93,],[15,15,22,15,15,15,15,]),'expressionBo':([14,16,27,34,36,37,38,56,75,76,89,90,],[21,31,49,55,58,59,60,49,84,84,84,84,]),'expressionAR':([14,16,27,34,36,37,38,39,40,41,42,43,44,45,46,47,48,56,62,75,76,79,89,90,],[23,23,50,54,23,23,23,61,63,64,65,66,67,68,69,70,71,77,80,83,83,86,83,83,]),'listID':([75,76,89,90,],[82,85,95,96,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> PACKAGE MAIN IMPORT STRING FUNC MAIN LPAREN RPAREN LCURLBRACKET list RCURLBRACKET','statement',11,'p_statement_expr','plintax.py',19),
  ('statement -> PACKAGE MAIN IMPORT STRING FUNC MAIN LPAREN RPAREN LCURLBRACKET RCURLBRACKET','statement',10,'p_statement_expr','plintax.py',20),
  ('list -> inst','list',1,'p_list','plintax.py',29),
  ('list -> inst list','list',2,'p_list','plintax.py',30),
  ('assignment -> ID ASSIGN expressionAR','assignment',3,'p_assignment','plintax.py',37),
  ('assignment -> ID ASSIGN expressionBo','assignment',3,'p_assignment','plintax.py',38),
  ('inst -> FOR expressionBo LCURLBRACKET list RCURLBRACKET','inst',5,'p_inst_For','plintax.py',44),
  ('inst -> FOR assignment SEMICOLON expressionBo SEMICOLON expressionAR LCURLBRACKET list RCURLBRACKET','inst',9,'p_inst_For','plintax.py',45),
  ('inst -> assignment SEMICOLON','inst',2,'p_inst_assignment','plintax.py',53),
  ('inst -> IF expressionBo LCURLBRACKET list RCURLBRACKET ELSE LCURLBRACKET list RCURLBRACKET','inst',9,'p_inst_If','plintax.py',58),
  ('inst -> IF expressionBo LCURLBRACKET list RCURLBRACKET','inst',5,'p_inst_If','plintax.py',59),
  ('listID -> expressionAR','listID',1,'p_listID','plintax.py',66),
  ('listID -> expressionBo','listID',1,'p_listID','plintax.py',67),
  ('listID -> expressionBo COMMA listID','listID',3,'p_listID','plintax.py',68),
  ('listID -> expressionAR COMMA listID','listID',3,'p_listID','plintax.py',69),
  ('inst -> FMT POINT PRINT LPAREN listID RPAREN SEMICOLON','inst',7,'p_inst_func','plintax.py',85),
  ('inst -> FMT POINT SCAN LPAREN listID RPAREN SEMICOLON','inst',7,'p_inst_func','plintax.py',86),
  ('expressionAR -> expressionAR PLUS expressionAR','expressionAR',3,'p_expressionAR_binop','plintax.py',94),
  ('expressionAR -> expressionAR MINUS expressionAR','expressionAR',3,'p_expressionAR_binop','plintax.py',95),
  ('expressionAR -> expressionAR TIMES expressionAR','expressionAR',3,'p_expressionAR_binop','plintax.py',96),
  ('expressionAR -> expressionAR DIVIDE expressionAR','expressionAR',3,'p_expressionAR_binop','plintax.py',97),
  ('expressionAR -> INT','expressionAR',1,'p_expressionAR_int','plintax.py',116),
  ('expressionAR -> FLOAT','expressionAR',1,'p_expressionAR_float','plintax.py',121),
  ('expressionAR -> LPAREN expressionAR RPAREN','expressionAR',3,'p_expressionAR_group','plintax.py',126),
  ('expressionBo -> expressionAR MORE expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',134),
  ('expressionBo -> expressionAR LESS expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',135),
  ('expressionBo -> expressionAR MOREEQUAL expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',136),
  ('expressionBo -> expressionAR LESSEQUAL expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',137),
  ('expressionBo -> expressionBo NOTEQUAL expressionBo','expressionBo',3,'p_expressionBo_binop','plintax.py',138),
  ('expressionBo -> expressionAR NOTEQUAL expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',139),
  ('expressionBo -> expressionBo EQUALSTO expressionBo','expressionBo',3,'p_expressionBo_binop','plintax.py',140),
  ('expressionBo -> expressionAR EQUALSTO expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',141),
  ('expressionBo -> ID','expressionBo',1,'p_expressionBo_binop','plintax.py',142),
  ('expressionBo -> TRUE','expressionBo',1,'p_expressionBo_int','plintax.py',168),
  ('expressionBo -> FALSE','expressionBo',1,'p_expressionBo_int','plintax.py',169),
  ('expressionBo -> LPAREN expressionBo RPAREN','expressionBo',3,'p_expressionBo_group','plintax.py',177),
]
