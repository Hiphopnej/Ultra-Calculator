class Node:
    def to_string(self):
        raise NotImplementedError

class Value(Node):
    def __init__(self, value):
        self.value = value

    def to_string(self):
        return str(self.value)

class Variable(Node):
    def __init__(self, name):
        self.name = name

    def to_string(self):
        return self.name

class BinaryOp(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def to_string(self):
        return f"{self.left.to_string()} {self.operator} {self.right.to_string()}"

class Equation:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_string(self):
        return f"{self.left.to_string()} = {self.right.to_string()}"