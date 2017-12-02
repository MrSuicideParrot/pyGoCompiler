import tree


class Tabela(dict):

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
                        self[i.children[0].value[1]] = self.dic_tipos[i.children[1].value[0]]
                    else:
                        print('ERROR: Assignement of already existent variable')
                        exit(1)
                elif type(i) is tree.Equalizer:
                    var = i.children[0].value[1]
                    if var in self:
                        if self[var] != self.dic_tipos[i.children[1].value[0]]:
                            print('ERROR: variable does not type')
                            exit(1)
                    else:
                        print('ERROR: variable does not exist')
                        exit(1)

                else:
                    self.create(i)

        except AttributeError:
            pass
