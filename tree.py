# -*- coding: utf-8 -*-

from treelib import Tree, Node
import InterCode


class Elemento():
    tabela = None

    rAvaliable = {
        's':[InterCode.Register('$s' + str(i)) for i in reversed(range(8))],
        't':[InterCode.Register('$t' + str(i)) for i in reversed(range(8))],
        'a':[InterCode.Register('$a' + str(i)) for i in reversed(range(4))],
    }

    l = -1

    @staticmethod
    def getVar(t='t'):
        if Elemento.rAvaliable[t]:
            return Elemento.rAvaliable[t].pop()
        else:
            if t == 's':
                return None
            print("Insufficient register number!")
            exit(1)

    @staticmethod
    def freeVar(t, s=True):
        if t.rType() == 's':
            if s:
                Elemento.tabela.free(t)
            else:
                return

        Elemento.rAvaliable[t.rType()].append(t)

    @staticmethod
    def getLabel():
        Elemento.l += 1
        return 'label' + str(Elemento.l)

    @staticmethod
    def disAlloc(args):
        for i in args:
            if type(i) is InterCode.Register:
                Elemento.freeVar(i, False)

    @staticmethod
    def setTable(tabela):
        Elemento.tabela = tabela

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
            if type(i) != ExprAr and type(i) != Group:
                if type(i) == Number:
                    tmp = Elemento.getVar()
                    lista.append(InterCode.LI(tmp, i.value[1]))
                    arg.append(tmp)
                    continue
                arg.append(Elemento.tabela[i.value[1]].getReg(lista))
            else:
                tmp = Elemento.getVar()
                lista += i.recInstr(tmp)
                arg.append(tmp)

        lista.append(InterCode.Expr(self.value[1], var, *arg))
        Elemento.disAlloc(arg)

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
            if type(i) != ExprBo and type(i) != ExprAr:
                if type(i) == Boolean or type(i) == Number:
                    tmp = Elemento.getVar()
                    lista.append(InterCode.LI(tmp,int(i.value[1])))
                    arg.append(tmp)
                    continue
                arg.append(Elemento.tabela[i.value[1]].getReg(lista))
            else:
                tmp = Elemento.getVar()
                lista += i.recInstr(tmp)
                arg.append(tmp)

        lista.append(InterCode.Expr(self.value[1], var, *arg))
        Elemento.disAlloc(arg)

        return lista

    """Label de verdade"""
    def initIF(self, flag):
        lista = []
        arg = []
        for i in self.children:
            if type(i) != ExprBo and type(i) != ExprAr:
                if type(i) == Boolean or type(i) == Number:
                    tmp = Elemento.getVar()
                    lista.append(InterCode.LI(tmp, int(i.value[1])))
                    arg.append(tmp)
                    continue

                arg.append(Elemento.tabela[i.value[1]].getReg(lista))
            else:
                tmp = Elemento.getVar()
                lista += i.recInstr(tmp)
                arg.append(tmp)

        arg.append(flag)

        if self.value[1] != '&&' and self.value[1] != '||' :
            lista.append(InterCode.Branch(self.value[1], *arg))
        else:
            "Caso para quando é && ou ||"
            lista.append(InterCode.BIN(self.value[1], arg[0], arg[1]))
            lista.append(InterCode.Branch("==", arg[0], 1, flag)) # temos de confirmar isto

        Elemento.disAlloc(arg)
        return lista


class Identifier(Elemento):
    def __init__(self, value):
        self.value = ('ID', value)


class Number(Elemento):
    def __init__(self, value):
        self.value = ('NUMBER', value)


class Boolean(Elemento):
    def __init__(self, value):
        self.value = ('BOOL', value)

    """Partimos do principio que a flag será para onde que saltar se for verdadeiro a condição
    os booleanos serão representados por inteiros 1 -> true e 0 -> false """

    def initIF(self, flag):
        return [InterCode.Branch('==', int(self.value[1]), 1, flag)]


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

        inst = self.children[0].initIF(l1)

        """Else"""
        if len(self.children) == 3:
            inst += self.children[2].recInstr()
        inst.append(InterCode.GoTo(l3))

        """IF"""
        inst.append(InterCode.Label(l1))
        inst += self.children[1].recInstr()

        """RETOMA AO CODIGO NORMAL"""
        inst.append(InterCode.Label(l3))
        return inst


class For(Elemento):
    def __init__(self, iniciacao=None, condicao=None, incremento=None, body=None):
        self.value = ('FOR',)
        self.children = []
        self.tipo = [ None for _ in range(4)]
        if iniciacao:
            self.children.append(iniciacao)
            self.tipo[0] = iniciacao

        if condicao:
            self.children.append(condicao)
            self.tipo[1] = condicao

        if incremento:
            self.children.append(incremento)
            self.tipo[2] = incremento

        self.children.append(body)
        self.tipo[3] = body

    def recInstr(self):
        inst = []
        l1 = Elemento.getLabel() # bg
        l2 = Elemento.getLabel() # first
        l3 = Elemento.getLabel() # end
        '''Inicialização'''
        if self.tipo[0]:
            inst += self.tipo[0].recInstr()

        inst.append(InterCode.Label(l1))
        inst += self.tipo[1].initIF(l2)
        inst.append(InterCode.GoTo(l3))

        inst.append(InterCode.Label(l2))
        inst += self.tipo[3].recInstr()

        '''Incremento'''
        if self.tipo[2]:
            inst += self.tipo[2].recInstr()

        inst.append(InterCode.GoTo(l1))
        inst.append(InterCode.Label(l3))
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
            if type(i) != ExprBo and type(i) != ExprAr:
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
            if type(self.children[1]) == Boolean or type(self.children[1]) == Number:
                a1 = Elemento.getVar()
                inst.append(InterCode.LI(a1, int(self.children[1].value[1])))
            else:
                a1 = Elemento.tabela[self.children[1].value[1]].getReg(inst)
        else:
            a1 = Elemento.getVar()
            inst = self.children[1].recInstr(a1)

        tmp = Elemento.tabela[self.children[0].value[1]].getReg(inst)
        inst.append(InterCode.Atr(None,tmp,a1))

        return inst


class Equalizer(Elemento):
    def __init__(self, ID, value):
        self.value = ('EQUALS', '=')
        self.children = []
        self.children.append(Identifier(ID))
        self.children.append(value)

    def recInstr(self):
        inst = []
        if type(self.children[1]) != ExprAr and type(self.children[1]) != ExprBo:
            if type(self.children[1]) == Boolean or type(self.children[1]) == Number:
                a1 = Elemento.getVar()
                inst.append(InterCode.LI(a1, int(self.children[1].value[1])))
            else:
                a1 = Elemento.tabela[self.children[1].value[1]].getReg(inst)
        else:
            a1 = Elemento.getVar()
            inst = self.children[1].recInstr(a1)

        tmp = Elemento.tabela[self.children[0].value[1]].getReg(inst)
        inst.append(InterCode.Atr(None, tmp, a1))

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
        if self.children[0].value[0] == 'LIST':
            return self.children[0].recInstr()
        else:
            return self.children[0].recInstr(self.value[1])


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

    def recInstr(self, func):
        lista = []
        left = self.children[0]
        try:
            right = self.children[1]
        except IndexError:
            right = None

        "Analise se é um scan ou print"
        if func == 'Scan':
            lista.append(InterCode.Syscall(5,Elemento.tabela[left].getReg(lista)))
        elif func == 'Print':
            if type(left) != ExprAr and type(left) != ExprBo:
                if type(left) == Boolean or type(left):
                    arg = left.value[1]
                else:
                    arg = Elemento.tabela[left.value[1]].getReg(lista)
            else:
                    arg = Elemento.getVar('t')
                    lista = lista + left.recInstr(arg)

            lista.append(InterCode.Syscall(1,arg))      # Só imprime Inteiros

            if right:  # Imprime espaço
                lista.append(InterCode.Syscall(11,32))

        "Caso para progredir com a recursão"
        if right:
            lista = lista + right.recInstr(func)

        return lista

    def list(self):
        ret = [self.children[0]]
        try:
            ret += self.children[1].list()
        except IndexError:
            pass

        return ret

