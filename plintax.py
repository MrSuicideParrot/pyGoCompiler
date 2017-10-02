# -*- coding: utf-8 -*-

from ploken import tokens
from ply import yacc as yacc


def p_expression(p):
    '''expression: expression PLUS expression
                 | expression MINUS expression
                 | expression TIMES expression
                 | expression DIVIDE expression
                 | LPAREN expression RPAREN
                 | PLUS NUMBER
                 | MINUS NUMBER
                 | NUMBER
                 | FLOAT'''

    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        else:
            p[0] = p[2]
    elif len(p) == 3:
        pass



# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
