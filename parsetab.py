
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLESSMOREEQUALSTOMOREEQUALLESSEQUALNOTEQUALleftPLUSMINUSleftTIMESDIVIDErightUMINUSINT FLOAT PLUS MINUS TIMES DIVIDE EQUALS LPAREN RPAREN LCURLBRACKET RCURLBRACKET ID COMMENT STRING ASSIGN SEMICOLON COMMA POINT NOT EQUALSTO MORE LESS MOREEQUAL LESSEQUAL NOTEQUAL INCREMENT DECREMENT BREAK CASE CHAN CONST CONTINUE DEFAULT DEFER ELSE FALLTHROUGH FOR FUNC GO GOTO IF IMPORT INTERFACE MAP PACKAGE RANGE RETURN SELECT STRUCT SWITCH TYPE VAR MAIN FMT PRINT SCAN TRUE FALSEstatement : PACKAGE MAIN IMPORT STRING FUNC MAIN LPAREN RPAREN LCURLBRACKET list RCURLBRACKET\n                 | PACKAGE MAIN IMPORT STRING FUNC MAIN LPAREN RPAREN LCURLBRACKET RCURLBRACKETlist : inst\n            | inst listassignment : ID ASSIGN expressionAR\n                  | ID ASSIGN expressionBo\n                  | ID EQUALS expressionAR\n                  | ID EQUALS expressionBo\n                  | ID INCREMENT\n                  | ID DECREMENTinst : FOR expressionBo LCURLBRACKET list RCURLBRACKET\n            | FOR assignment SEMICOLON expressionBo SEMICOLON assignment LCURLBRACKET list RCURLBRACKETinst : assignment SEMICOLONinst : IF expressionBo LCURLBRACKET list RCURLBRACKET ELSE LCURLBRACKET list RCURLBRACKET\n            | IF expressionBo LCURLBRACKET list RCURLBRACKETlistID : expressionAR\n              | expressionBo\n              | expressionBo COMMA listID\n              | expressionAR COMMA listIDIDlist : ID\n              | ID COMMA IDlistinst : FMT POINT PRINT LPAREN listID RPAREN SEMICOLON\n            | FMT POINT SCAN LPAREN IDlist RPAREN SEMICOLON\n            | FMT POINT PRINT LPAREN RPAREN SEMICOLON\n            | FMT POINT SCAN LPAREN RPAREN SEMICOLONexpressionAR : expressionAR PLUS expressionAR\n                    | expressionAR MINUS expressionAR\n                    | expressionAR TIMES expressionAR\n                    | expressionAR DIVIDE expressionAR\n                    | IDexpressionAR : INTexpressionAR : MINUS expressionAR %prec UMINUSexpressionAR : FLOATexpressionAR : LPAREN expressionAR RPARENexpressionBo : expressionAR MORE expressionAR\n                    | expressionAR LESS expressionAR\n                    | expressionAR MOREEQUAL expressionAR\n                    | expressionAR LESSEQUAL expressionAR\n                    | expressionBo NOTEQUAL expressionBo\n                    | expressionAR NOTEQUAL expressionAR\n                    | expressionBo EQUALSTO expressionBo\n                    | expressionAR EQUALSTO expressionARexpressionBo : NOT expressionBo %prec UMINUSexpressionBo : TRUE\n                    | FALSEexpressionBo : LPAREN expressionBo RPAREN'
    
_lr_action_items = {'PACKAGE':([0,],[2,]),'$end':([1,12,19,],[0,-2,-1,]),'MAIN':([2,6,],[3,7,]),'IMPORT':([3,],[4,]),'STRING':([4,],[5,]),'FUNC':([5,],[6,]),'LPAREN':([7,14,16,24,27,29,36,37,41,42,43,44,45,46,47,48,49,50,51,52,53,58,60,61,64,85,102,103,],[8,27,27,27,27,58,64,64,27,27,27,58,58,58,58,58,58,58,58,58,58,58,85,86,64,64,64,64,]),'RPAREN':([8,25,26,30,31,34,54,55,56,57,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,85,86,87,91,93,94,95,97,110,111,113,],[9,-44,-45,-31,-33,-30,-43,81,82,-32,-39,-41,-35,-36,-37,-38,-40,-42,-26,-27,-28,-29,-46,-34,82,92,96,82,100,-16,-17,104,-20,-19,-18,-21,]),'LCURLBRACKET':([9,21,25,26,30,31,33,34,38,39,54,57,62,63,65,66,68,69,71,72,73,74,75,76,77,78,79,80,81,82,98,99,],[10,40,-44,-45,-31,-33,59,-30,-9,-10,-43,-32,-5,-6,-7,-8,-39,-41,-35,-36,-37,-38,-40,-42,-26,-27,-28,-29,-46,-34,107,108,]),'RCURLBRACKET':([10,11,13,20,32,67,84,88,90,101,105,109,112,114,115,116,117,],[12,19,-3,-4,-13,88,90,-11,-15,-24,-25,-22,-23,116,117,-12,-14,]),'FOR':([10,13,32,40,59,88,90,101,105,107,108,109,112,116,117,],[14,14,-13,14,14,-11,-15,-24,-25,14,14,-22,-23,-12,-14,]),'IF':([10,13,32,40,59,88,90,101,105,107,108,109,112,116,117,],[16,16,-13,16,16,-11,-15,-24,-25,16,16,-22,-23,-12,-14,]),'FMT':([10,13,32,40,59,88,90,101,105,107,108,109,112,116,117,],[17,17,-13,17,17,-11,-15,-24,-25,17,17,-22,-23,-12,-14,]),'ID':([10,13,14,16,24,27,29,32,36,37,40,41,42,43,44,45,46,47,48,49,50,51,52,53,58,59,64,85,86,88,89,90,101,102,103,105,106,107,108,109,112,116,117,],[18,18,28,34,34,34,34,-13,34,34,18,34,34,34,34,34,34,34,34,34,34,34,34,34,34,18,34,34,97,-11,18,-15,-24,34,34,-25,97,18,18,-22,-23,-12,-14,]),'NOT':([14,16,24,27,36,37,41,42,43,64,85,102,103,],[24,24,24,24,24,24,24,24,24,24,24,24,24,]),'TRUE':([14,16,24,27,36,37,41,42,43,64,85,102,103,],[25,25,25,25,25,25,25,25,25,25,25,25,25,]),'FALSE':([14,16,24,27,36,37,41,42,43,64,85,102,103,],[26,26,26,26,26,26,26,26,26,26,26,26,26,]),'INT':([14,16,24,27,29,36,37,41,42,43,44,45,46,47,48,49,50,51,52,53,58,64,85,102,103,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'MINUS':([14,16,23,24,27,28,29,30,31,34,36,37,41,42,43,44,45,46,47,48,49,50,51,52,53,56,57,58,62,64,65,71,72,73,74,75,76,77,78,79,80,82,83,85,87,93,102,103,],[29,29,51,29,29,-30,29,-31,-33,-30,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,51,-32,29,51,29,51,51,51,51,51,51,51,-26,-27,-28,-29,-34,51,29,51,51,29,29,]),'FLOAT':([14,16,24,27,29,36,37,41,42,43,44,45,46,47,48,49,50,51,52,53,58,64,85,102,103,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'SEMICOLON':([15,22,25,26,30,31,34,38,39,54,57,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,92,96,100,104,],[32,43,-44,-45,-31,-33,-30,-9,-10,-43,-32,-5,-6,-7,-8,-39,-41,89,-35,-36,-37,-38,-40,-42,-26,-27,-28,-29,-46,-34,101,105,109,112,]),'POINT':([17,],[35,]),'ASSIGN':([18,28,],[36,36,]),'EQUALS':([18,28,],[37,37,]),'INCREMENT':([18,28,],[38,38,]),'DECREMENT':([18,28,],[39,39,]),'NOTEQUAL':([21,23,25,26,28,30,31,33,34,54,55,56,57,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,87,93,94,],[41,48,-44,-45,-30,-31,-33,41,-30,-43,41,48,-32,48,41,48,41,None,None,41,-35,-36,-37,-38,-40,-42,-26,-27,-28,-29,-46,-34,48,48,41,]),'EQUALSTO':([21,23,25,26,28,30,31,33,34,54,55,56,57,62,63,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,87,93,94,],[42,49,-44,-45,-30,-31,-33,42,-30,-43,42,49,-32,49,42,49,42,None,None,42,-35,-36,-37,-38,-40,-42,-26,-27,-28,-29,-46,-34,49,49,42,]),'MORE':([23,28,30,31,34,56,57,62,65,77,78,79,80,82,87,93,],[44,-30,-31,-33,-30,44,-32,44,44,-26,-27,-28,-29,-34,44,44,]),'LESS':([23,28,30,31,34,56,57,62,65,77,78,79,80,82,87,93,],[45,-30,-31,-33,-30,45,-32,45,45,-26,-27,-28,-29,-34,45,45,]),'MOREEQUAL':([23,28,30,31,34,56,57,62,65,77,78,79,80,82,87,93,],[46,-30,-31,-33,-30,46,-32,46,46,-26,-27,-28,-29,-34,46,46,]),'LESSEQUAL':([23,28,30,31,34,56,57,62,65,77,78,79,80,82,87,93,],[47,-30,-31,-33,-30,47,-32,47,47,-26,-27,-28,-29,-34,47,47,]),'PLUS':([23,28,30,31,34,56,57,62,65,71,72,73,74,75,76,77,78,79,80,82,83,87,93,],[50,-30,-31,-33,-30,50,-32,50,50,50,50,50,50,50,50,-26,-27,-28,-29,-34,50,50,50,]),'TIMES':([23,28,30,31,34,56,57,62,65,71,72,73,74,75,76,77,78,79,80,82,83,87,93,],[52,-30,-31,-33,-30,52,-32,52,52,52,52,52,52,52,52,52,52,-28,-29,-34,52,52,52,]),'DIVIDE':([23,28,30,31,34,56,57,62,65,71,72,73,74,75,76,77,78,79,80,82,83,87,93,],[53,-30,-31,-33,-30,53,-32,53,53,53,53,53,53,53,53,53,53,-28,-29,-34,53,53,53,]),'COMMA':([25,26,30,31,34,54,57,68,69,71,72,73,74,75,76,77,78,79,80,81,82,93,94,97,],[-44,-45,-31,-33,-30,-43,-32,-39,-41,-35,-36,-37,-38,-40,-42,-26,-27,-28,-29,-46,-34,102,103,106,]),'PRINT':([35,],[60,]),'SCAN':([35,],[61,]),'ELSE':([90,],[99,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'list':([10,13,40,59,107,108,],[11,20,67,84,114,115,]),'inst':([10,13,40,59,107,108,],[13,13,13,13,13,13,]),'assignment':([10,13,14,40,59,89,107,108,],[15,15,22,15,15,98,15,15,]),'expressionBo':([14,16,24,27,36,37,41,42,43,64,85,102,103,],[21,33,54,55,63,66,68,69,70,55,94,94,94,]),'expressionAR':([14,16,24,27,29,36,37,41,42,43,44,45,46,47,48,49,50,51,52,53,58,64,85,102,103,],[23,23,23,56,57,62,65,23,23,23,71,72,73,74,75,76,77,78,79,80,83,87,93,93,93,]),'listID':([85,102,103,],[91,110,111,]),'IDlist':([86,106,],[95,113,]),}

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
  ('list -> inst','list',1,'p_list','plintax.py',28),
  ('list -> inst list','list',2,'p_list','plintax.py',29),
  ('assignment -> ID ASSIGN expressionAR','assignment',3,'p_assignment','plintax.py',36),
  ('assignment -> ID ASSIGN expressionBo','assignment',3,'p_assignment','plintax.py',37),
  ('assignment -> ID EQUALS expressionAR','assignment',3,'p_assignment','plintax.py',38),
  ('assignment -> ID EQUALS expressionBo','assignment',3,'p_assignment','plintax.py',39),
  ('assignment -> ID INCREMENT','assignment',2,'p_assignment','plintax.py',40),
  ('assignment -> ID DECREMENT','assignment',2,'p_assignment','plintax.py',41),
  ('inst -> FOR expressionBo LCURLBRACKET list RCURLBRACKET','inst',5,'p_inst_For','plintax.py',55),
  ('inst -> FOR assignment SEMICOLON expressionBo SEMICOLON assignment LCURLBRACKET list RCURLBRACKET','inst',9,'p_inst_For','plintax.py',56),
  ('inst -> assignment SEMICOLON','inst',2,'p_inst_assignment','plintax.py',64),
  ('inst -> IF expressionBo LCURLBRACKET list RCURLBRACKET ELSE LCURLBRACKET list RCURLBRACKET','inst',9,'p_inst_If','plintax.py',69),
  ('inst -> IF expressionBo LCURLBRACKET list RCURLBRACKET','inst',5,'p_inst_If','plintax.py',70),
  ('listID -> expressionAR','listID',1,'p_listID','plintax.py',77),
  ('listID -> expressionBo','listID',1,'p_listID','plintax.py',78),
  ('listID -> expressionBo COMMA listID','listID',3,'p_listID','plintax.py',79),
  ('listID -> expressionAR COMMA listID','listID',3,'p_listID','plintax.py',80),
  ('IDlist -> ID','IDlist',1,'p_IDlist','plintax.py',87),
  ('IDlist -> ID COMMA IDlist','IDlist',3,'p_IDlist','plintax.py',88),
  ('inst -> FMT POINT PRINT LPAREN listID RPAREN SEMICOLON','inst',7,'p_inst_func','plintax.py',104),
  ('inst -> FMT POINT SCAN LPAREN IDlist RPAREN SEMICOLON','inst',7,'p_inst_func','plintax.py',105),
  ('inst -> FMT POINT PRINT LPAREN RPAREN SEMICOLON','inst',6,'p_inst_func','plintax.py',106),
  ('inst -> FMT POINT SCAN LPAREN RPAREN SEMICOLON','inst',6,'p_inst_func','plintax.py',107),
  ('expressionAR -> expressionAR PLUS expressionAR','expressionAR',3,'p_expressionAR_binop','plintax.py',117),
  ('expressionAR -> expressionAR MINUS expressionAR','expressionAR',3,'p_expressionAR_binop','plintax.py',118),
  ('expressionAR -> expressionAR TIMES expressionAR','expressionAR',3,'p_expressionAR_binop','plintax.py',119),
  ('expressionAR -> expressionAR DIVIDE expressionAR','expressionAR',3,'p_expressionAR_binop','plintax.py',120),
  ('expressionAR -> ID','expressionAR',1,'p_expressionAR_binop','plintax.py',121),
  ('expressionAR -> INT','expressionAR',1,'p_expressionAR_int','plintax.py',136),
  ('expressionAR -> MINUS expressionAR','expressionAR',2,'p_expressionAR_inverse','plintax.py',141),
  ('expressionAR -> FLOAT','expressionAR',1,'p_expressionAR_float','plintax.py',146),
  ('expressionAR -> LPAREN expressionAR RPAREN','expressionAR',3,'p_expressionAR_group','plintax.py',151),
  ('expressionBo -> expressionAR MORE expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',158),
  ('expressionBo -> expressionAR LESS expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',159),
  ('expressionBo -> expressionAR MOREEQUAL expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',160),
  ('expressionBo -> expressionAR LESSEQUAL expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',161),
  ('expressionBo -> expressionBo NOTEQUAL expressionBo','expressionBo',3,'p_expressionBo_binop','plintax.py',162),
  ('expressionBo -> expressionAR NOTEQUAL expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',163),
  ('expressionBo -> expressionBo EQUALSTO expressionBo','expressionBo',3,'p_expressionBo_binop','plintax.py',164),
  ('expressionBo -> expressionAR EQUALSTO expressionAR','expressionBo',3,'p_expressionBo_binop','plintax.py',165),
  ('expressionBo -> NOT expressionBo','expressionBo',2,'p_expressionBo_inverse','plintax.py',182),
  ('expressionBo -> TRUE','expressionBo',1,'p_expressionBo_int','plintax.py',188),
  ('expressionBo -> FALSE','expressionBo',1,'p_expressionBo_int','plintax.py',189),
  ('expressionBo -> LPAREN expressionBo RPAREN','expressionBo',3,'p_expressionBo_group','plintax.py',197),
]
