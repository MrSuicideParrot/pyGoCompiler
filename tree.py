from binarytree import Node, pprint


class Expr:

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '/': lambda x, y: x / y,
        '*': lambda x, y: x * y,
    }

    def gettype(self):
        return self.value[0]

    @staticmethod
    def eval(m1):
        if m1.gettype() == "NUMBER":
            return m1.value
        elif m1.gettype() == "OPERATION":
            try:
                vleft = Expr.eval(m1.left)
            except AttributeError:
                vleft = 0

            try:
                vright = Expr.eval(m1.right)
            except AttributeError:
                vright = 0

            return Expr.operations[m1.operator](vleft, vright)


class Expr_number(Expr, Node):
    def __init__(self, value):
        self.value = ("NUMBER", value)
        self.left = None
        self.right = None


class Expr_oper(Expr, Node):
    def __init__(self, operator, left, right):
        self.value = ("OPERATION", operator)
        self.left = left
        self.right = right

"""
class Expr_id(Expr):
    def __init__(self, name, valueArray):
        self.name = name
        self.valueArray = valueArray
        self.type = 'ID'
"""