# -*- coding: utf-8 -*-

from treelib import Tree, Node as node_failed

class Node(node_failed):
    def


class Prog(Tree):
    pass


class ListCommand(Node):
    def __init__(self, left, right):
        """
        :param left: Elemento da lista de comandos
        :type left: Node
        :param right: Resto da lista de comandos
        :type right: ListCommand
        """
        self.ADD(left)
        self.ADD(right)


class ExprAr(Node):
    def __init__(self, operator, left, right):
        """
        :type operator: str
        :type left: ExprAr | Number | Identifier
        :type right: ExprAr | Number | Identifier
        """
        self.tag = ('OPERATOR_AR', operator)
        self.ADD(left.identifier)
        self.ADD(right.identifier)


class ExprBo(Node):
    def __init__(self, operator, left, right):
        """
        :type operator: str
        :type left: ExprBo | Number | Identifier
        :type right: ExprBo | Number | Identifier
        """
        self.tag = ('OPERATOR_AR',operator)
        self.ADD(left)
        self.ADD(right)


class Identifier(Node):
    def __init__(self, value):
        self.tag = ('ID',value)


class Number(Node):
    def __init__(self, value):
        self.tag = ('NUMBER', value)


class Boolean(Node):
    def __init__(self, value):
        self.tag = ('BOOL', value)


class Branch(Node):
    def __init__(self, condicao, ifbody, elsebody=None):
        self.tag = ('BRANCH',)
        self.ADD(condicao)
        self.ADD(ifbody)
        if elsebody is not None:
            self.ADD(elsebody)


class For(Node):
    def __init__(self, condicao, body):
        self.tag = ('FOR',)
        self.ADD(condicao)
        self.ADD(body)