
class Instruction:
    def __init__(self, op, e1=None, e2=None, e3=None):
        self.op = op
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3

    def  __str__(self):
        inst = self.op
        if self.e1:
            inst += ' ' + self.e1
        elif self.e2:
            inst += ', ' + self.e2
        elif self.e3:
            inst += ', ' + self.e3

        return inst

    @staticmethod
    def genCode(arvore):
        pass
