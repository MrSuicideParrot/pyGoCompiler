# -*- coding: utf-8 -*-

from treelib import Tree, Node


class Elemento():

    def pprint(self):
        tree_print = Tree()
        parent = tree_print.create_node(tag=str(self.value))

        for i in self.children:
            i.__recpprint(tree_print, parent.identifier)

        print(tree_print)

    def __recpprint(self, arvore, parent):
        """
        :param tree: treelib.Tree
        :param parent: str
        """
        actual = arvore.create_node(tag=str(self.value), parent=parent)

        try:
            for i in self.children:
                if issubclass(type(i), Elemento):
                    i.__recpprint(arvore, actual.identifier)
                else:  # Em principio já não é necessário
                    arvore.create_node(tag=str(i), parent=actual.identifier)
        except AttributeError:
            pass


class Programa(Elemento):
    def __init__(self, lista):
        self.value = ('ROOT',)
        self.children = lista

# Estrutura do programa
class Package(Elemento):
    def __init__(self, pacote):
        self.value = ('PACKAGE',pacote)
        self.children = []


class Import(Elemento):
    def __init__(self,biblio):
        self.value = ('IMPORT',biblio)
        self.children = []

class ListCommand(Elemento):
    def __init__(self, left, right=None):
        """
        :param left: Elemento da lista de comandos
        :type left: Elemento
        :param right: Resto da lista de comandos
        :type right: ListCommand
        """
        self.value = ('LIST',)
        self.children = []
        self.children.append(left)
        if right:
            self.children.append(right)


class ExprAr(Elemento):
    def __init__(self, operator, left, right=None):
        """
        :type operator: str
        :type left: ExprAr | Number | Identifier
        :type right: ExprAr | Number | Identifier
        """
        self.value = ('OPERATOR_AR', operator)
        self.children = []
        self.children.append(left)
        if right:
            self.children.append(right)


class ExprBo(Elemento):
    def __init__(self, operator, left, right=None):
        """
        :type operator: str
        :type left: ExprBo | Number | Identifier
        :type right: ExprBo | Number | Identifier
        """
        self.value = ('OPERATOR_AR', operator)
        self.children = []
        self.children.append(left)
        if right:
            self.children.append(right)


class Identifier(Elemento):
    def __init__(self, value):
        self.value = ('ID', value)


class Number(Elemento):
    def __init__(self, value):
        self.value = ('NUMBER', value)


class Boolean(Elemento):
    def __init__(self, value):
        self.value = ('BOOL', value)


class Branch(Elemento):
    def __init__(self, condicao, ifbody, elsebody=None):
        self.value = ('BRANCH',)
        self.children = []
        self.children.append(condicao)
        self.children.append(ifbody)
        if elsebody:
            self.children.append(elsebody)


class For(Elemento):
    def __init__(self, iniciacao=None, condicao=None, incremento=None, body=None):
        self.value = ('FOR',)
        self.children = []

        if iniciacao:
            self.children.append(iniciacao)

        if condicao:
            self.children.append(condicao)

        if incremento:
            self.children.append(incremento)

        self.children.append(body)


class Group(Elemento):
    def __init__(self, valor):
        self.value = ('GROUP',)
        self.children = []
        self.children.append(valor)


class Assignment(Elemento):
    def __init__(self, ID, valor):
        self.value = ('ASSIGN', ':=')
        self.children = []
        self.children.append(Identifier(ID))
        self.children.append(valor)


class Equalizer(Elemento):
    def __init__(self, ID, value):
        self.value = ('EQUALS', '=')
        self.children = []
        self.children.append(Identifier(ID))
        self.children.append(value)


class Func(Elemento):
    def __init__(self, tipo, argv=None, lista=None):
        """"
        :param tipo: Nome da função
        :type str
        :param argv: Lista de argumentos da função
        :type list()
        :param lista: Próximas instruções
        :type ListCommand
        """
        self.value = ('FUNC', tipo)

        self.children = []

        if argv:
            self.children.append(argv)

        if lista:
            self.children.append(lista)

class ListPRI(ListCommand):
    def __init__(self, left, right=None):
        """
        :param left: Elemento da lista de comandos
        :type left: Elemento
        :param right: Resto da lista de comandos
        :type right: ListCommand
        """
        self.value = ('ARGV',)
        self.children = []
        self.children.append(left)
        if right:
            self.children.append(right)