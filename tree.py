class Expr:

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '/': lambda x, y: x / y,
        '*': lambda x, y: x * y,
    }

    def gettype(self):
        return self.type

    @staticmethod
    def eval(m1):
        if m1.type == "NUMBER":
            return m1.value
        elif m1.type == "OPERATION":
            try:
                vleft = Expr.eval(m1.left)
            except AttributeError:
                vleft = 0

            try:
                vright = Expr.eval(m1.right)
            except AttributeError:
                vright = 0

            return Expr.operations[m1.operator](vleft, vright)



class Expr_number(Expr):
    def __init__(self, value):
        self.value = value
        self.type = "NUMBER"


class Expr_oper(Expr):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right
        self.type = "OPERATION"
