
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

        if self.e3:
            buf = '\t'
            buf += instr[self.op]
            buf += " "
            buf += self.e1
            buf += ", "
            buf += self.e2
            buf += ", "
            buf += self.e3
            buf += "\n"
        elif self.op == '-':
            buf = '\tsub '
            buf += self.e1
            buf += ", "
            buf += self.e2
            buf += ", $zero\n"
        else:
            print("ERRO")
            exit(1)

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
        buf += ", $zero\n"
        fd.write(buf)


"""OP registo  registo2  label"""
class Branch(Instruction):
    def __str__(self):
        return 'if '+str(self.e1)+self.op+str(self.e2)+' goto '+self.e3

    def translate(self, fd):
        inst = {
            '<':'\tslt $t0, '+str(self.e1)+', '+str(self.e2)+'\n\t'+'bne $t0, $zero, '+self.e3,
            '>':'\tslt $t0, '+str(self.e2)+', '+str(self.e1)+'\n\t'+'bne $t0, $zero, '+self.e3,
            '<=':'\tslt $t0, '+str(self.e2)+', '+str(self.e1)+'\n\t'+'beq $t0, $zero, '+self.e3,
            '>=':'\tslt $t0, '+str(self.e1)+', '+str(self.e2)+'\n\t'+'beq $t0, $zero, '+self.e3,
            '==':'\tbeq '+str(self.e1)+', '+str(self.e2)+', '+self.e3, # temos de estar preparados porque acho que a direita temos numeros e nao registos talvez usar o BGTZ
        }

        fd.write(inst[self.op])

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
            fd.write("\tadd "+str(self.e1)+", $v0, $zero\n")
        else:
            fd.write("\tadd $a0, " + str(self.e1) +", $zero\n")
            fd.write("\tsyscall\n")


class Register(str):
    def rType(self):
        return self[1]


class BIN(Instruction):
    def __str__(self):
        return self.op+" "+self.e2+" "+self.e3

    def translate(self, fd):
        inst = {
            '&&':'and',
            '||':'or',
        }
        fd.write("\t"+inst[self.op]+" "+self.e1+", "+self.e2+", "+self.e3)


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
