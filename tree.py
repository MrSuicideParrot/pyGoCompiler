# -*- coding: utf-8 -*-

class Node:
    pass


class Programa(Node):
    def __init__(self, lista):
        self.children = []
        self.children.append(lista)


class ListCommand(Node):
    def __init__(self, left, right=None):
        """
        :param left: Elemento da lista de comandos
        :type left: Node
        :param right: Resto da lista de comandos
        :type right: ListCommand
        """
        self.children = []
        self.children.append(left)
        self.children.append(right)


class ExprAr(Node):
    def __init__(self, operator, left, right):
        """
        :type operator: str
        :type left: ExprAr | Number | Identifier
        :type right: ExprAr | Number | Identifier
        """
        self.value = ('OPERATOR_AR', operator)
        self.children = []
        self.children.append(left)
        self.children.append(right)


class ExprBo(Node):
    def __init__(self, operator, left, right):
        """
        :type operator: str
        :type left: ExprBo | Number | Identifier
        :type right: ExprBo | Number | Identifier
        """
        self.tag = ('OPERATOR_AR', operator)
        self.children = []
        self.children.append(left)
        self.children.append(right)

class Identifier(Node):
    def __init__(self, value):
        self.value = ('ID', value)


class Number(Node):
    def __init__(self, value):
        self.value = ('NUMBER', value)


class Boolean(Node):
    def __init__(self, value):
        self.value = ('BOOL', value)


class Branch(Node):
    def __init__(self, condicao, ifbody, elsebody=None):
        self.value = ('BRANCH',)
        self.children = []
        self.children.append(condicao)
        self.children.append(ifbody)
        self.children.append(elsebody)


class For(Node):
    def __init__(self, condicao, body):
        self.value = ('FOR',)
        self.children = []
        self.children.append(condicao)
        self.children.append(body)

class Group(Node):
    def __init__(self, valor):
        self.value = ('GROUP',)
        self.children = []
        self.children.append(valor)


class Assignment(Node):
    def __init__(self, ID, valor):
        self.value = ('EQUALS', '=')
        self.children = []
        self.children.append(ID)
        self.children.append(valor)


class Func(Node):
    def __init__(self, tipo, argv, lista):
        """"
        :param tipo: Nome da função
        :type str
        :param argv: Lista de argumentos da função
        :type list()
        :param lista: Próximas instruções
        :type ListCommand
        """
        self.value = ('FUNC', tipo)
        self.children = argv
        self.children = lista