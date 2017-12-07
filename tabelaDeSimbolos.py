import tree
import InterCode


class Tabela(dict):

    class Variavel:
        def __init__(self, out, var, tipo):
            """
            :param out: apontador para própria tabela
            :param var: Nome da variaver
            :param tipo: Tipo da variavel
            """
            self.out = out
            self.tipo = tipo
            self.var = var
            self.registo = None

        def getType(self):
            return self.tipo

        def haveRegister(self):
            if self.registo:
                return True
            return False

        def getReg(self, lista):
            if self.registo:
                return self.registo
            else:
                tmp = tree.Elemento.getVar('s')
                """
                Caso existam registos disponiveis
                    aloca-o caso contrário guarda um na heap e volta a alocar registo
                """
                if not tmp:
                    for i in self.out.values():
                        if not i.haveRegister():
                            """Store value"""
                            lista.append(InterCode.Store(i.var,i.registo))

                            tree.Elemento.freeVar(i.registo)
                            i.registo = None
                            break

                    tmp = tree.Elemento.getVar('s')

                lista.append(InterCode.Load(self.var,tmp))
                self.registo = tmp
                return tmp


    dic_tipos = {'OPERATOR_AR':'NUMBER',
                 'NUMBER':'NUMBER',
                 'OPERATOR_BO':'BOOL',
                 'BOOL':'BOOL'}

    def __init__(self, arvore):
        dict.__init__(self)
        self.create(arvore)

    def create(self, elem):
        """ DFS """
        try:
            for i in elem.children:
                """
                Parti do principio que não se pode declarar variáveis duas vezes
                """
                if type(i) is tree.Assignment:
                    if i.children[0].value[1] not in self:
                        if i.children[1].value[0] is 'ID':
                            tipo = self[i.children[1].value[1]].getType()
                        else:
                            tipo = self.dic_tipos[i.children[1].value[0]]
                        self[i.children[0].value[1]] = self.Variavel(self, i.children[0].value[1], tipo)
                    else:
                        print('ERROR: Assignement of already existent variable')
                        exit(1)
                elif type(i) is tree.Equalizer:
                    var = i.children[0].value[1]
                    if var in self:
                        if self[var].getType() != self.dic_tipos[i.children[1].value[0]]:
                            print('ERROR: variable does not type')
                            exit(1)
                    else:
                        print('ERROR: variable does not exist')
                        exit(1)

                elif type(i) is tree.Func and i.value[1] == "Scan":
                    lista = i.children[0].list()
                    for c in lista:
                        if c not in self:
                            self[c] = self.Variavel(self, i.value[1], 'NUMBER' ) # Nao podemos perver tipos

                else:
                    self.create(i)

        except AttributeError:
            pass

    def free(self, reg):
        for i in self.values():
            if i.registo == reg:
                i.registo = None
                break

    def createData(self, fd):
        for i in self.values():
            fd.write('\t'+i.var+" .word 0\n")