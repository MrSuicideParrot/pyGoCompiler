# -*- coding: utf-8 -*-

from ploken import tokens, lexer
from ply import yacc as yacc

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# variaveis = {}

"""
def p_assignment(p):
    '''assignment : VAR EQUALS expression'''
    variaveis[p[1]] = p[3]
"""


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''

    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_inverse(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[1]


def p_expression_int(p):
    'expression : INT'
    p[0] = p[1]


def p_expression_float(p):
    'expression : FLOAT'
    p[0] = p[1]


def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


"""
def p_expression_var(p):
    'expression : VAR'
    try:
        p[0] = variaveis[p[1]]
    except LookupError:
        print("Undifened valua")
        p[0] = 0
"""


# Error rule for syntax errors
def p_error(p):
    print(p)


# Build the parser
parser = yacc.yacc()


def main():
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result)


if __name__ == '__main__':
    main()
