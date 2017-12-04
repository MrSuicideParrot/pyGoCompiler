
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

    def translate(self, fd):
        instr = {
            "+":"add",
            "-":"sub",
            "*":"mul",
            "/":"div",
        }

        buf = '\t'
        buf += instr[self.op]
        buf += " "
        buf += self.e1
        buf += ", "
        buf += self.e2
        buf += ", "
        buf += self.e3
        buf += "\n"

        fd.write(buf)


class Atr(Instruction):
    def __str__(self):
        inst = str(self.e1)
        inst += '='
        inst += str(self.e2)

        return  inst

    def translate(self, fd):
        if type(self.e2) == int:
            buf = "\tli "
        else:
            buf = "\tmove "
        buf += self.e1
        buf += ", "
        buf += str(self.e2)
        buf += "\n"
        fd.write(buf)


"""OP registo  registo2  label"""
class Branch(Instruction):
    def __str__(self):
        return 'if '+str(self.e1)+self.op+str(self.e2)+' goto '+self.e3

    def translate(self, fd):
        inst = {
            '<':'algo',
            '>':'algo',
            '<=':'algo',
            '>=':'algo',
        }

        fd.write('\t'+inst[self.op]+" "+str(self.e1)+", "+str(self.e2)+", "+self.e3)

'''op = Label'''
class GoTo(Instruction):
    def __str__(self):
        return '\tgoto '+self.op

    def translate(self, fd):
        fd.write("\tj "+self.op+"\n")


'''op=Label'''
class Label(Instruction):
    def __str__(self):
        return 'label '+self.op

    def translate(self, fd):
        fd.write(self.op+":\n")

"""
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

    def translate(self, fd):
        buf = '\t'
        if self.op == 'read':
            Load('$v0',5).translate(fd)
            
        else:
            pass
"""

"""op=variavel reg"""
class Load(Instruction):
    def __str__(self):
        return "lw "+self.e1+", "+self.op

    def translate(self, fd):
        fd.write("\tlw "+self.e1+", "+self.op+"\n")


"""op=variavel reg"""
class Store(Instruction):
    def __str__(self):
        return "sw "+self.e1+", "+self.op

    def translate(self, fd):
        fd.write("\tsw "+self.e1+", "+self.op+"\n")


"""op = registo e1 = valor"""
class LI(Instruction):
    def __str__(self):
        return "li "+self.op+" "+str(self.e1)

    def translate(self, fd):
        fd.write("\tli "+self.op+", "+str(self.e1)+"\n")


"""op=code of syscall"""
class Syscall(Instruction):
    def __str__(self):
        return "syscall "+str(self.op)+" "+str(self.e1)

    def translate(self, fd):
        LI('$v0', self.op).translate(fd)

        if self.op == 5: # caso seja scan
            fd.write("\tsyscall\n")
            fd.write("\tmove "+str(self.e1)+", $v0\n")
        else:
            fd.write("\tmove $a0, " + str(self.e1) +"\n")
            fd.write("\tsyscall\n")


class Register(str):
    def rType(self):
        return self[1]


def printASM(file, instr3):
    """
    :param file: ficheiro
    :param instr3: lista de instruções de três elementos
    :return:
    """
    fd = open(file, "w")

    for i in instr3:
        i.translate(fd)

    fd.close()
