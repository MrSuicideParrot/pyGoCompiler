# -*- coding: utf-8 -*-

from ply import lex as lex

#words reserved to the go language
reservedw = {
    'break' : 'BREAK',
    'case' : 'CASE',
    'chan' : 'CHAN',
    'const' : 'CONST',
    'continue' : 'CONTINUE',
    'default' : 'DEFAULT',
    'defer' : 'DEFER',
    'else' : 'ELSE',
    'fallthrough' : 'FALLTHROUGH',
    'for' : 'FOR',
    'func' : 'FUNC',
    'go' : 'GO',
    'goto' : 'GOTO',
    'if' : 'IF',
    'import' : 'IMPORT',
    'interface' : 'INTERFACE',
    'map' : 'MAP',
    'package' : 'PACKAGE',
    'range' : 'RANGE',
    'return' : 'RETURN',
    'select' : 'SELECT',
    'struct' : 'STRUCT',
    'switch' : 'SWITCH',
    'type' : 'TYPE',
    'var' : 'VAR'
}

# Tuple of token names.
tokens = [
    'INT',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN',
    'RPAREN',
  #  'VARIABLE',
    'ID',
    'COMMENT'
] + list(reservedw.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
#t_VARIABLE = r'[a-zA-Z] [a-zA-Z0-9]*'


# regular expression rule to Float numbers
def t_FLOAT(t):
    r'\d + \.\d+'
    t.value = float(t.value)
    return t


# A regular expression rule to Int numbers
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservedw.get(t.value,'ID') #check for reserved words
    return t

def t_COMMENT(t):
    r'//.*'
    pass #token discarded

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


# função para testes do analisador léxico
def main():
    data = input()

    global lexer
    lexer.input(data)

    while True:
        tok = lexer.token()

        if not tok:
            break

        print(tok)


if __name__ == '__main__':
    main()
