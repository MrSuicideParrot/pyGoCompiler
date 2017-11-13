import tree


class Tabela(dict):

    dic_tipos = {'OPERATOR_AR':'NUMBER',
                 'NUMBER':'NUMBER',
                 'OPERATOR_BO':'BOOL',
                 'BOOL':'BOOL'}

    def create(self, elem):
        """ DFS """
        try:
            for i in elem.children:
                """
                Parti do principio que não se pode declarar variáveis duas vezes
                """
                if i is tree.Assignment:
                    if i.children[0].value not in self:
                        self[i.children[0].value] = self.dic_tipos[i.children[1].value]
                    else:
                        print('ERROR: Assignement of already existent variable')
                        exit(1)
                elif i is tree.Equalizer:
                    var = i.children[0].value
                    if var in self:
                        if self[var] != self.dic_tipos[i.children[1].value]:
                            print('ERROR: variable does not type')
                            exit(1)
                    else:
                        print('ERROR: variable does not exist')
                        exit(1)

                else:
                    self.create(i)

        except AttributeError:
            pass
