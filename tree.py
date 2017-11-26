# -*- coding: utf-8 -*-

from treelib import Tree, Node
import InterCode


class Elemento():
    t = -1
    l = -1

    @staticmethod
    def getVar():
        Elemento.t += 1
        return 't'+str(Elemento.t)

    @staticmethod
    def getLabel():
        Elemento.l += 1
        return 'label' + str(Elemento.l)

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

    def recInstr(self):
        return []

class Programa(Elemento):
    def __init__(self, lista):
        self.value = ('ROOT',)
        self.children = lista

    def recInstr(self):
        lista = []
        for i in self.children:
            lista += i.recInstr()
        return lista

    def getInstructionList(self):
        return self.recInstr()


# Estrutura do programa
class Package(Elemento):
    def __init__(self, pacote):
        self.value = ('PACKAGE',pacote)
        self.children = []

    def recInstr(self):
        return [InterCode.Label(self.value[1])]


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

    def recInstr(self):
        lista = []
        for i in self.children:
            lista += i.recInstr()

        return lista


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

    def recInstr(self, var):
        lista = []
        arg = []
        for i in self.children:
            if type(i) != ExprAr:
                arg.append(i.value[1])
            else:
                tmp = Elemento.getVar()
                lista += i.recInstr(tmp)
                arg.append(tmp)

        lista.append(InterCode.Expr(self.value[1], var, *arg))

        return lista


class ExprBo(Elemento):
    def __init__(self, operator, left, right=None):
        """
        :type operator: str
        :type left: ExprBo | Number | Identifier
        :type right: ExprBo | Number | Identifier
        """
        self.value = ('OPERATOR_BO', operator)
        self.children = []
        self.children.append(left)
        if right:
            self.children.append(right)

    def recInstr(self, var):
        lista = []
        arg = []
        for i in self.children:
            if type(i) != (ExprBo|ExprAr):
                arg.append(i.value[1])
            else:
                tmp = Elemento.getVar()
                lista += i.recInstr(tmp)
                arg.append(tmp)

        lista.append(InterCode.Expr(self.value[1], var, *arg))

        return lista

    def __initIF(self, flag):
        lista = []
        arg = []
        for i in self.children:
            if type(i) != (ExprBo | ExprAr):
                arg.append(i.value[1])
            else:
                tmp = Elemento.getVar()
                lista += i.recInstr(tmp)
                arg.append(tmp)
        arg.append(flag)
        lista.append(InterCode.Branch(self.value[1], *arg))

        return lista
    """"
    def invserse(self):
    
        }"""


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

    def recInstr(self):
        l1 = Elemento.getLabel() #verdaeiro

        l3 = Elemento.getLabel() # retoma

        inst = self.children[0].__initIF(l1)
        if len(self.children == 3):
            inst += self.children[2].recInstr()
        inst.append(InterCode.GoTo(l3))
        inst.append(InterCode.Label(l1))
        inst += self.children[1].recInstr()
        inst.append(InterCode.Label(l3))
        return inst


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

    def recInstr(self):
        inst = []
        l1 = Elemento.getLabel() # bg
        l2 = Elemento.getLabel() # first
        l3 = Elemento.getLabel() # end
        '''Inicialização'''
        inst += self.children[0].recInstr()
        inst.append(InterCode.Label(l1))
        inst += self.children[1].__initIF(l2)
        inst.append(InterCode.GoTo(l3))
        inst.append(InterCode.Label(l2))
        inst += self.children[3].recInstr()
        inst += self.children[2].recInstr()
        inst.append(InterCode.GoTo(l1))

        return inst


class Group(Elemento):
    def __init__(self, valor):
        self.value = ('GROUP',)
        self.children = []
        self.children.append(valor)

    def recInstr(self, var):
        lista = []
        a1 = None
        a2 = None
        for i in self.children:
            if type(i) != (ExprBo | ExprAr):
                a1 = i.value
            else:
                a2 = Elemento.getVar()
                lista += i.recInstr(a2)

        #lista.append(InterCode.Expr(self.value[1], var, a1, a2))

        return lista


class Assignment(Elemento):
    def __init__(self, ID, valor):
        self.value = ('ASSIGN', ':=')
        self.children = []
        self.children.append(Identifier(ID))
        self.children.append(valor)

    def recInstr(self):
        inst = []
        if type(self.children[1]) != ExprAr and type(self.children[1]) != ExprBo:
            a1 = self.children[1].value
        else:
            a1 = Elemento.getVar()
            inst = self.children[1].recInstr(a1)

        inst.append(InterCode.Atr(self.value[1],self.children[0],a1))

        return inst


class Equalizer(Elemento):
    def __init__(self, ID, value):
        self.value = ('EQUALS', '=')
        self.children = []
        self.children.append(Identifier(ID))
        self.children.append(value)

    def recInstr(self):
        inst = []
        if type(self.children[1]) != (ExprAr | ExprBo):
            a1 = self.children[1].value
        else:
            a1 = Elemento.getVar()
            inst.append(self.children[1].recInstr(a1))

        inst.append(InterCode.Atr(self.value[1], a1))

        return inst


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

    def recInstr(self):
        lista = []
        for i in self.children:
            lista = i.recInstr() + lista

        return lista

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

    def recInstr(self):
        lista = []
        for i in self.children:
            lista = i + lista

        return lista
