# -*- coding: utf-8 -*-

from binarytree import Node


class ListCommand(Node):
    def __init__(self, left, right):
        """
        :param left: Elemento da lista de comandos
        :type left: Node
        :param right: Resto da lista de comandos
        :type right: ListCommand
        """
        self.left = left
        self.right = right


class ExprAr(Node):
    def __init__(self, operator, left, right):
        """
        :type operator: str
        :type left: ExprAr | Number | Identifier
        :type right: ExprAr | Number | Identifier
        """
        self.value = ('OPERATOR_AR', operator)
        self.left = left
        self.right = right


class ExprBo(Node):
    def __init__(self, operator, left, right):
        """
        :type operator: str
        :type left: ExprBo | Number | Identifier
        :type right: ExprBo | Number | Identifier
        """
        self.tag = ('OPERATOR_AR', operator)
        self.left = left
        self.right = right


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
        self.left = condicao
        self.right = BranchBody(ifbody, elsebody)


class BranchBody(Node):
    def __init__(self, ifbody, elsebody):
        self.value = ('BRANCHOTIONS',)
        self.left = ifbody
        self.right = elsebody


class For(Node):
    def __init__(self, condicao, body):
        self.value = ('FOR',)
        self.left = condicao
        self.right = body
