

class Node:
    pass

class Expession:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Assignment(Expession):
    pass

class ID:
    def __init__(self, name):
        self.name = name

class LPAREN:
    pass

class RPAREN:
    pass

class FLOAT(float):
    pass

class INT(int):
    pass