# -*- coding: utf-8 -*-

from ploken import tokens, lexer
from ply import yacc as yacc
from tree import *

precedence = (
    ('nonassoc', 'LESS', 'MORE', 'EQUALSTO','MOREEQUAL',
    'LESSEQUAL', 'NOTEQUAL' ),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# variaveis = {}


def p_statement_expr(t):
    '''statement : PACKAGE MAIN IMPORT STRING FUNC MAIN LPAREN RPAREN LCURLBRACKET list RCURLBRACKET
                 | PACKAGE MAIN IMPORT STRING FUNC MAIN LPAREN RPAREN LCURLBRACKET RCURLBRACKET'''
    if len(t) == 11:
        t[0] = Programa([Package(t[2]), Import(t[4]), Func(t[6], None, None)])
    else:
        t[0] = Programa([Package(t[2]), Import(t[4]), Func(t[6], None, t[10])])
    t[0].pprint()


def p_list(p):
    '''list : inst
            | inst list'''
    if len(p) == 2:
        p[0] = ListCommand(p[1])
    else:
        p[0] = ListCommand(p[1], p[2])

def p_assignment(p):
    '''assignment : ID ASSIGN expressionAR
                  | ID ASSIGN expressionBo
                  | ID EQUALS expressionAR
                  | ID EQUALS expressionBo
                  | ID INCREMENT
                  | ID DECREMENT'''
    if len(p) == 3:
        if p[2] == '++':
            p[0] = Equalizer(Identifier(p[1]),ExprAr('+',Identifier(p[1]),Number(1)))
        else:
            p[0] = Equalizer(Identifier(p[1]), ExprAr('-', Identifier(p[1]), Number(1)))
    else:
        if p[2] == '=':
            p[0] = Equalizer(p[1], p[3])
        else:
            p[0] = Assignment(p[1], p[3])

# Faltam os for mais complicados
def p_inst_For(p):
    '''inst : FOR expressionBo LCURLBRACKET list RCURLBRACKET
            | FOR assignment SEMICOLON expressionBo SEMICOLON assignment LCURLBRACKET list RCURLBRACKET'''
    if len(p) == 6:
        p[0] = For(condicao=p[2],body=p[4])
    else:
        p[0] = For(iniciacao=p[2], condicao=p[4], incremento=p[6], body=p[8])


def p_inst_assignment(p):
    'inst : assignment SEMICOLON'
    p[0] = p[1]


def p_inst_If(p):
    '''inst : IF expressionBo LCURLBRACKET list RCURLBRACKET ELSE LCURLBRACKET list RCURLBRACKET
            | IF expressionBo LCURLBRACKET list RCURLBRACKET'''
    if len(p) == 10:
        p[0] = Branch(p[2], p[4], p[8])
    else:
        p[0] = Branch(p[2], p[4])

def p_listID(p):
    '''listID : expressionAR
              | expressionBo
              | expressionBo COMMA listID
              | expressionAR COMMA listID'''
    if len(p) == 2:
        p[0] = ListPRI(p[1])
    else:
        p[0] = ListPRI(p[1], p[3])

"""
def p_inst_expression(p):
    '''inst : expressionAR
            | expressionBo'''
    p[0] = p[1]

"""
#Funções

def p_inst_func(p):
    '''inst : FMT POINT PRINT LPAREN listID RPAREN SEMICOLON
            | FMT POINT SCAN LPAREN listID RPAREN SEMICOLON
            | FMT POINT PRINT LPAREN RPAREN SEMICOLON
            | FMT POINT SCAN LPAREN RPAREN SEMICOLON'''
    try:
        p[0] = Func(p[3],p[5])
    except IndexError:
        p[0] = Func(p[3])


#---------------------------------------------------------
# operações ariteméticas
def p_expressionAR_binop(p):
    '''expressionAR : expressionAR PLUS expressionAR
                    | expressionAR MINUS expressionAR
                    | expressionAR TIMES expressionAR
                    | expressionAR DIVIDE expressionAR
                    | ID'''
    if len(p) == 4:
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


def p_expressionAR_int(p):
    'expressionAR : INT'
    p[0] = Number(p[1])


def p_expressionAR_inverse(p):
    'expressionAR : MINUS expressionAR %prec UMINUS'
    p[0] = ExprAr('-', p[2])


def p_expressionAR_float(p):
    'expressionAR : FLOAT'
    p[0] = Number(p[1])


def p_expressionAR_group(p):
    'expressionAR : LPAREN expressionAR RPAREN'
    p[0] = Group(p[2])


# ---------------------------------------------------------
# operações booleanas
def p_expressionBo_binop(p):
    '''expressionBo : expressionAR MORE expressionAR
                    | expressionAR LESS expressionAR
                    | expressionAR MOREEQUAL expressionAR
                    | expressionAR LESSEQUAL expressionAR
                    | expressionBo NOTEQUAL expressionBo
                    | expressionAR NOTEQUAL expressionAR
                    | expressionBo EQUALSTO expressionBo
                    | expressionAR EQUALSTO expressionAR'''
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



def p_expressionBo_inverse(p):
    'expressionBo : NOT expressionBo %prec UMINUS'
    p[0] = ExprBo('!', p[2])



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
    print("Erro ",end='')
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
        fd = open("example1.go", "r")
        result = parser.parse(''.join(fd.readlines()))


if __name__ == '__main__':
    main()
