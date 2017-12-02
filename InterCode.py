
class Instruction:
    def __init__(self, op, e1=None, e2=None, e3=None):
        self.op = op
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3

    def __str__(self):
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


class Expr(Instruction):
    def __str__(self):
        inst = str(self.e1)
        inst += '='
        inst += str(self.e2)
        inst += str(self.op)
        inst += str(self.e3)

        return inst


class Atr(Instruction):
    def __str__(self):
        inst = str(self.e1)
        inst += '='
        inst += str(self.e2)

        return  inst


class Jump(Instruction):
    def __str__(self):
        return 'goto'+self.e1


"""OP registo  registo2  label"""
class Branch(Instruction):
    def __str__(self):
        return 'if '+str(self.e1)+self.op+str(self.e2)+' goto '+self.e3


'''op = Label'''
class GoTo(Instruction):
    def __str__(self):
        return 'goto '+self.op


'''op=Label'''
class Label(Instruction):
    def __str__(self):
        return 'label '+self.op


class Function(Instruction):
    def __str__(self):
        if self.op == 'read':
            inst = self.e1
            inst += ':='
            inst += self.op +'()'

        else:
            inst = self.op
            inst +='('
            inst += self.e1
            inst += ')'

        return inst


"""op=variavel reg"""
class Load(Instruction):
    def __str__(self):
        return "lw "+self.e1+", "+self.op


"""op=variavel reg"""
class Store(Instruction):
    def __str__(self):
        return "sw "+self.e1+", "+self.op


class Register(str):
    def rType(self):
        return self[1]

"""op=code of syscall"""
class Syscall(Instruction):
    def __str__(self):
        return "syscall "+str(self.op)+" "+str(self.e1)