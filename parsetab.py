
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLESSMOREEQUALSTOMOREEQUALLESSEQUALNOTEQUALleftPLUSMINUSleftTIMESDIVIDErightUMINUSINT FLOAT PLUS MINUS TIMES DIVIDE EQUALS LPAREN RPAREN LCURLBRACKET RCURLBRACKET ID COMMENT STRING ASSIGN SEMICOLON COMMA POINT NOT EQUALSTO MORE LESS MOREEQUAL LESSEQUAL NOTEQUAL BREAK CASE CHAN CONST CONTINUE DEFAULT DEFER ELSE FALLTHROUGH FOR FUNC GO GOTO IF IMPORT INTERFACE MAP PACKAGE RANGE RETURN SELECT STRUCT SWITCH TYPE VAR MAIN FMT PRINT SCAN TRUE FALSEstatement : PACKAGE MAIN IMPORT STRING FUNC MAIN LPAREN RPAREN LCURLBRACKET list RCURLBRACKET\n                 | PACKAGE MAIN IMPORT STRING FUNC MAIN LPAREN RPAREN LCURLBRACKET RCURLBRACKETlist : inst\n            | inst listassignment : ID ASSIGN expressionAR\n                  | ID ASSIGN expressionBo\n                  | ID EQUALS expressionAR\n                  | ID EQUALS expressionBoinst : FOR expressionBo LCURLBRACKET list RCURLBRACKET\n            | FOR assignment SEMICOLON expressionBo SEMICOLON expressionAR LCURLBRACKET list RCURLBRACKETinst : assignment SEMICOLONinst : IF expressionBo LCURLBRACKET list RCURLBRACKET ELSE LCURLBRACKET list RCURLBRACKET\n            | IF expressionBo LCURLBRACKET list RCURLBRACKETlistID : expressionAR\n              | expressionBo\n              | expressionBo COMMA listID\n              | expressionAR COMMA listIDinst : FMT POINT PRINT LPAREN listID RPAREN SEMICOLON\n            | FMT POINT SCAN LPAREN listID RPAREN SEMICOLONexpressionAR : expressionAR PLUS expressionAR\n                     | expressionAR MINUS expressionAR\n                     | expressionAR TIMES expressionAR\n                     | expressionAR DIVIDE expressionAR\n                     | IDexpressionAR : INTexpressionAR : MINUS expressionAR %prec UMINUSexpressionAR : FLOATexpressionAR : LPAREN expressionAR RPARENexpressionBo : expressionAR MORE expressionAR\n                    | expressionAR LESS expressionAR\n                    | expressionAR MOREEQUAL expressionAR\n                    | expressionAR LESSEQUAL expressionAR\n                    | expressionBo NOTEQUAL expressionBo\n                    | expressionAR NOTEQUAL expressionAR\n                    | expressionBo EQUALSTO expressionBo\n                    | expressionAR EQUALSTO expressionARexpressionBo : NOT expressionBo %prec UMINUSexpressionBo : TRUE\n                    | FALSEexpressionBo : LPAREN expressionBo RPAREN'
    
_lr_action_items = {'PACKAGE':([0,],[2,]),'$end':([1,12,19,],[0,-2,-1,]),'MAIN':([2,6,],[3,7,]),'IMPORT':([3,],[4,]),'STRING':([4,],[5,]),'FUNC':([5,],[6,]),'LPAREN':([7,14,16,24,27,29,36,37,39,40,41,42,43,44,45,46,47,48,49,50,51,56,58,59,62,83,84,87,96,97,],[8,27,27,27,27,56,62,62,27,27,27,56,56,56,56,56,56,56,56,56,56,56,83,84,62,62,62,56,62,62,]),'RPAREN':([8,25,26,30,31,34,52,53,54,55,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,85,89,90,91,92,102,103,],[9,-38,-39,-25,-27,-24,-37,79,80,-26,-33,-35,-29,-30,-31,-32,-34,-36,-20,-21,-22,-23,-40,-28,80,80,95,-14,-15,98,-17,-16,]),'LCURLBRACKET':([9,21,25,26,30,31,33,34,52,55,66,67,69,70,71,72,73,74,75,76,77,78,79,80,93,94,],[10,38,-38,-39,-25,-27,57,-24,-37,-26,-33,-35,-29,-30,-31,-32,-34,-36,-20,-21,-22,-23,-40,-28,99,100,]),'RCURLBRACKET':([10,11,13,20,32,65,82,86,88,101,104,105,106,107,108,],[12,19,-3,-4,-11,86,88,-9,-13,-18,-19,107,108,-10,-12,]),'FOR':([10,13,32,38,57,86,88,99,100,101,104,107,108,],[14,14,-11,14,14,-9,-13,14,14,-18,-19,-10,-12,]),'IF':([10,13,32,38,57,86,88,99,100,101,104,107,108,],[16,16,-11,16,16,-9,-13,16,16,-18,-19,-10,-12,]),'FMT':([10,13,32,38,57,86,88,99,100,101,104,107,108,],[17,17,-11,17,17,-9,-13,17,17,-18,-19,-10,-12,]),'ID':([10,13,14,16,24,27,29,32,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,62,83,84,86,87,88,96,97,99,100,101,104,107,108,],[18,18,28,34,34,34,34,-11,34,34,18,34,34,34,34,34,34,34,34,34,34,34,34,34,34,18,34,34,34,-9,34,-13,34,34,18,18,-18,-19,-10,-12,]),'NOT':([14,16,24,27,36,37,39,40,41,62,83,84,96,97,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'TRUE':([14,16,24,27,36,37,39,40,41,62,83,84,96,97,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'FALSE':([14,16,24,27,36,37,39,40,41,62,83,84,96,97,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'INT':([14,16,24,27,29,36,37,39,40,41,42,43,44,45,46,47,48,49,50,51,56,62,83,84,87,96,97,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'MINUS':([14,16,23,24,27,28,29,30,31,34,36,37,39,40,41,42,43,44,45,46,47,48,49,50,51,54,55,56,60,62,63,69,70,71,72,73,74,75,76,77,78,80,81,83,84,85,87,90,93,96,97,],[29,29,49,29,29,-24,29,-25,-27,-24,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,49,-26,29,49,29,49,49,49,49,49,49,49,-20,-21,-22,-23,-28,49,29,29,49,29,49,49,29,29,]),'FLOAT':([14,16,24,27,29,36,37,39,40,41,42,43,44,45,46,47,48,49,50,51,56,62,83,84,87,96,97,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'SEMICOLON':([15,22,25,26,30,31,34,52,55,60,61,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,95,98,],[32,41,-38,-39,-25,-27,-24,-37,-26,-5,-6,-7,-8,-33,-35,87,-29,-30,-31,-32,-34,-36,-20,-21,-22,-23,-40,-28,101,104,]),'POINT':([17,],[35,]),'ASSIGN':([18,28,],[36,36,]),'EQUALS':([18,28,],[37,37,]),'NOTEQUAL':([21,23,25,26,28,30,31,33,34,52,53,54,55,60,61,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,85,90,91,],[39,46,-38,-39,-24,-25,-27,39,-24,-37,39,46,-26,46,39,46,39,None,None,39,-29,-30,-31,-32,-34,-36,-20,-21,-22,-23,-40,-28,46,46,39,]),'EQUALSTO':([21,23,25,26,28,30,31,33,34,52,53,54,55,60,61,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,85,90,91,],[40,47,-38,-39,-24,-25,-27,40,-24,-37,40,47,-26,47,40,47,40,None,None,40,-29,-30,-31,-32,-34,-36,-20,-21,-22,-23,-40,-28,47,47,40,]),'MORE':([23,28,30,31,34,54,55,60,63,75,76,77,78,80,85,90,],[42,-24,-25,-27,-24,42,-26,42,42,-20,-21,-22,-23,-28,42,42,]),'LESS':([23,28,30,31,34,54,55,60,63,75,76,77,78,80,85,90,],[43,-24,-25,-27,-24,43,-26,43,43,-20,-21,-22,-23,-28,43,43,]),'MOREEQUAL':([23,28,30,31,34,54,55,60,63,75,76,77,78,80,85,90,],[44,-24,-25,-27,-24,44,-26,44,44,-20,-21,-22,-23,-28,44,44,]),'LESSEQUAL':([23,28,30,31,34,54,55,60,63,75,76,77,78,80,85,90,],[45,-24,-25,-27,-24,45,-26,45,45,-20,-21,-22,-23,-28,45,45,]),'PLUS':([23,28,30,31,34,54,55,60,63,69,70,71,72,73,74,75,76,77,78,80,81,85,90,93,],[48,-24,-25,-27,-24,48,-26,48,48,48,48,48,48,48,48,-20,-21,-22,-23,-28,48,48,48,48,]),'TIMES':([23,28,30,31,34,54,55,60,63,69,70,71,72,73,74,75,76,77,78,80,81,85,90,93,],[50,-24,-25,-27,-24,50,-26,50,50,50,50,50,50,50,50,50,50,-22,-23,-28,50,50,50,50,]),'DIVIDE':([23,28,30,31,34,54,55,60,63,69,70,71,72,73,74,75,76,77,78,80,81,85,90,93,],[51,-24,-25,-27,-24,51,-26,51,51,51,51,51,51,51,51,51,51,-22,-23,-28,51,51,51,51,]),'COMMA':([25,26,30,31,34,52,55,66,67,69,70,71,72,73,74,75,76,77,78,79,80,90,91,],[-38,-39,-25,-27,-24,-37,-26,-33,-35,-29,-30,-31,-32,-34,-36,-20,-21,-22,-23,-40,-28,96,97,]),'PRINT':([35,],[58,]),'SCAN':([35,],[59,]),'ELSE':([88,],[94,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'list':([10,13,38,57,99,100,],[11,20,65,82,105,106,]),'inst':([10,13,38,57,99,100,],[13,13,13,13,13,13,]),'assignment':([10,13,14,38,57,99,100,],[15,15,22,15,15,15,15,]),'expressionBo':([14,16,24,27,36,37,39,40,41,62,83,84,96,97,],[21,33,52,53,61,64,66,67,68,53,91,91,91,91,]),'expressionAR':([14,16,24,27,29,36,37,39,40,41,42,43,44,45,46,47,48,49,50,51,56,62,83,84,87,96,97,],[23,23,23,54,55,60,63,23,23,23,69,70,71,72,73,74,75,76,77,78,81,85,90,90,93,90,90,]),'listID':([83,84,96,97,],[89,92,102,103,]),}

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
  ('assignment -> ID EQUALS expressionAR','assignment',3,'p_assignment','plintax.py',39),
  ('assignment -> ID EQUALS expressionBo','assignment',3,'p_assignment','plintax.py',40),
  ('inst -> FOR expressionBo LCURLBRACKET list RCURLBRACKET','inst',5,'p_inst_For','plintax.py',55),
  ('inst -> FOR assignment SEMICOLON expressionBo SEMICOLON expressionAR LCURLBRACKET list RCURLBRACKET','inst',9,'p_inst_For','plintax.py',56),
  ('inst -> assignment SEMICOLON','inst',2,'p_inst_assignment','plintax.py',64),
  ('inst -> IF expressionBo LCURLBRACKET list RCURLBRACKET ELSE LCURLBRACKET list RCURLBRACKET','inst',9,'p_inst_If','plintax.py',69),
  ('inst -> IF expressionBo LCURLBRACKET list RCURLBRACKET','inst',5,'p_inst_If','plintax.py',70),
  ('listID -> expressionAR','listID',1,'p_listID','plintax.py',77),
  ('listID -> expressionBo','listID',1,'p_listID','plintax.py',78),
  ('listID -> expressionBo COMMA listID','listID',3,'p_listID','plintax.py',79),
  ('listID -> expressionAR COMMA listID','listID',3,'p_listID','plintax.py',80),
  ('inst -> FMT POINT PRINT LPAREN listID RPAREN SEMICOLON','inst',7,'p_inst_func','plintax.py',96),
  ('inst -> FMT POINT SCAN LPAREN listID RPAREN SEMICOLON','inst',7,'p_inst_func','plintax.py',97),
  ('expressionAR -> expressionAR PLUS expressionAR','expressionAR',3,'p_expressionAR_binop','plintax.py',105),
  ('expressionAR -> expressionAR MINUS expressionAR','expressionAR',3,'p_expressionAR_binop','plintax.py',106),
  ('expressionAR -> expressionAR TIMES expressionAR','expressionAR',3,'p_expressionAR_binop','plintax.py',107),
  ('expressionAR -> expressionAR DIVIDE expressionAR','expressionAR',3,'p_expressionAR_binop','plintax.py',108),
  ('expressionAR -> ID','expressionAR',1,'p_expressionAR_binop','plintax.py',109),
  ('expressionAR -> INT','expressionAR',1,'p_expressionAR_int','plintax.py',124),
  ('expressionAR -> MINUS expressionAR','expressionAR',2,'p_expressionAR_inverse','plintax.py',128),
  ('expressionAR -> FLOAT','expressionAR',1,'p_expressionAR_float','plintax.py',132),
  ('expressionAR -> LPAREN expressionAR RPAREN','expressionAR',3,'p_expressionAR_group','plintax.py',137),
  ('expressionBo -> expressionAR MORE expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',144),
  ('expressionBo -> expressionAR LESS expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',145),
  ('expressionBo -> expressionAR MOREEQUAL expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',146),
  ('expressionBo -> expressionAR LESSEQUAL expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',147),
  ('expressionBo -> expressionBo NOTEQUAL expressionBo','expressionBo',3,'p_expressionBo_binop','plintax.py',148),
  ('expressionBo -> expressionAR NOTEQUAL expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',149),
  ('expressionBo -> expressionBo EQUALSTO expressionBo','expressionBo',3,'p_expressionBo_binop','plintax.py',150),
  ('expressionBo -> expressionAR EQUALSTO expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',151),
  ('expressionBo -> NOT expressionBo','expressionBo',2,'p_expressionBo_inverse','plintax.py',168),
  ('expressionBo -> TRUE','expressionBo',1,'p_expressionBo_int','plintax.py',174),
  ('expressionBo -> FALSE','expressionBo',1,'p_expressionBo_int','plintax.py',175),
  ('expressionBo -> LPAREN expressionBo RPAREN','expressionBo',3,'p_expressionBo_group','plintax.py',183),
]
