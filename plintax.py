# -*- coding: utf-8 -*-

from ploken import tokens, lexer
from ply import yacc as yacc
from tree import *

precedence = (
    ('nonassoc', 'LESS', 'MORE', 'EQUALSTO','MOREEQUAL',
    'LESSEQUAL', 'NOTEQUAL' ),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
   # ('right', 'UMINUS'),
)

variaveis = {}


#tive que desativar isto
def p_statement_expr(t):
    'statement : FUNC MAIN LPAREN RPAREN LCURLBRACKET list RCURLBRACKET'
    t[0] = Func('MAIN',[],t[6])


def p_list(p):
    '''list : inst
            | inst list'''
    if len(p) == 2:
        p[0] = ListCommand(p[1])
    else:
        p[0] = ListCommand(p[1] + p[2])


def p_inst_assignment(p):
    '''inst : ID ASSIGN expressionAR
            | ID ASSIGN expressionBo'''
    p[0]=Assignment(p[2],p[1],p[3])


# Faltam os for mais complicados
def p_inst_For(p):
    '''inst : FOR expressionBo LCURLBRACKET list RCURLBRACKET'''
    p[0] = For(p[2],p[4])


def p_inst_If(p):
    '''inst : IF expressionBo LCURLBRACKET list RCURLBRACKET ELSE LCURLBRACKET list RCURLBRACKET
            | IF expressionBo LCURLBRACKET list RCURLBRACKET'''
    if p.len == 10:
        p[0] = Branch(p[2], p[4], p[9])
    else:
        p[0] = Branch(p[2], p[4])

def p_inst_expression(p):
    '''inst : expressionAR
            | expressionBo'''
    p[0] = p[1]

#---------------------------------------------------------
# operações ariteméticas
def p_expressionAR_binop(p):
    '''expressionAR : expressionAR PLUS expressionAR
                     | expressionAR MINUS expressionAR
                     | expressionAR TIMES expressionAR
                     | expressionAR DIVIDE expressionAR'''
    if p[2] == '+':
        p[0] = ExprAr('+', p[1], p[3])
    elif p[2] == '-':
        p[0] = ExprAr('-', p[1], p[3])
    elif p[2] == '*':
        p[0] = ExprAr('*', p[1], p[3])
    elif p[2] == '/':
     p[0] = ExprAr('/', p[1], p[3])
    else:
        p[0] = Identifier(p[1])

"""
def p_expressionAR_inverse(p):
    'expressionAR : MINUS expressionAR %prec UMINUS'
    p[0] = ExprAr('-', left=None, right=p[2].value)
"""

def p_expressionAR_int(p):
    'expressionAR : INT'
    p[0] = Number(p[1])


def p_expressionAR_float(p):
    'expressionAR : FLOAT'
    p[0] = Number(p[1])


def p_expressionAR_group(p):
    'expressionAR : LPAREN expressionAR RPAREN'
    p[0] = Group(p[2])



# ---------------------------------------------------------
# operações booleanas
def p_expressionBo_binop(p):
    '''expressionBo : expressionBo MORE expressionBo
                    | expressionBo LESS expressionBo
                    | expressionBo MOREEQUAL expressionBo
                    | expressionBo LESSEQUAL expressionBo
                    | expressionBo NOTEQUAL expressionBo
                    | expressionBo EQUALSTO expressionBo
                    | ID'''

    if p[2] == '>':
        p[0] = ExprBo('>', p[1], p[3])
    elif p[2] == '<':
        p[0] = ExprBo('<', p[1], p[3])
    elif p[2] == '>=':
        p[0] = ExprBo('>=', p[1], p[3])
    elif p[2] == '<=':
        p[0] = ExprBo('<=', p[1], p[3])
    elif p[2] == '!=':
        p[0] = ExprBo('!=', p[1], p[3])
    elif p[2] == '==':
        p[0] = ExprBo('==', p[1], p[3])
    else:
        p[0] = Identifier(p[1])


"""
def p_expressionBo_inverse(p):
    'expressionBo : MINUS expressionBo %prec UMINUS'
    p[0] = ExprBo('',(p[2].value))
"""


def p_expressionBo_int(p):
    '''expressionBo : TRUE
                    | FALSE'''
    if p[1] == 'true':
        p[0] = Boolean(True)
    else:
        p[0] = Boolean(False)


def p_expressionBo_group(p):
    'expressionBo : LPAREN expressionBo RPAREN'
    p[0] = Group(p[2])

# Error rule for syntax errors
def p_error(p):
    print(p)


# Build the parser
parser = yacc.yacc()


def main():
    file = False
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
        fd = open("exemplo1.txt", "r")
        parser.parse(''.join(fd.readlines()))


if __name__ == '__main__':
    main()
