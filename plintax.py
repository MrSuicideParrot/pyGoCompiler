# -*- coding: utf-8 -*-

from ploken import tokens, lexer
from ply import yacc as yacc
from tree import *

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

variaveis = {}

def p_statement_assignment(p):
    '''statement : ID EQUALS expression'''
    #p[0]=tree.Assignment('=',p[1],p[3])
    pass

"""def p_expr_list(p):
    '''expression : expression
                  |expression expr_list'''
    pass"""

def p_statement_expr(t):
    'statement : expression'
    print(Expr.eval(t[1]))


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''

    if p[2] == '+':
        p[0] = Expr_oper('+',p[1],p[3])
    elif p[2] == '-':
        p[0] = Expr_oper('-',p[1],p[3])
    elif p[2] == '*':
        p[0] = Expr_oper('*',p[1],p[3])
    elif p[2] == '/':
        p[0] = Expr_oper('/',p[1],p[3])


def p_expression_inverse(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = Expr_number('-',left=None, right=p[2])


def p_expression_int(p):
    'expression : INT'
    p[0] = Expr_number(p[1])


def p_expression_float(p):
    'expression : FLOAT'
    p[0] = Expr_number(p[1])


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    #p[0] = Expr_number(p[2],tree.LPAREN(),tree.RPAREN)
    pass

def p_expression_var(p):
    'expression : ID'
    p[0]= Expr_number(p[1].value)



# Error rule for syntax errors
def p_error(p):
    print(p)


# Build the parser
parser = yacc.yacc()


def main():
    file = True
    if not file:
        while True:
            try:
                s = input('calc > ')
            except EOFError:
                print()
                break
            if not s:
                continue
            result = parser.parse(s)
            if result is not None:
                print(result)
    else:
        fd = open("exemplo1.txt","r")
        result = parser.parse(fd.readlines())



if __name__ == '__main__':
    main()
