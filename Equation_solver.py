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

    def precedence(self):
        if self.operator in ("+", "-"):
            return 1
        if self.operator in ("*", "/"):
            return 2
        return 0

    def to_string(self):
        left = self.left.to_string()
        right = self.right.to_string()

        if isinstance(self.left, BinaryOp) and self.left.precedence() < self.precedence():
            left = f"({left})"

        if isinstance(self.right, BinaryOp) and self.right.precedence() < self.precedence():
            right = f"({right})"

        return f"{left} {self.operator} {right}"

class Equation:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_string(self):
        return f"{self.left.to_string()} = {self.right.to_string()}"

def parse_token(token):
    token = token.strip()

    if token == "x" or token == "-x":
        if token == "-x":
            return BinaryOp(
                Value(-1),
                "*",
                Variable("x")
            )

        return Variable("x")

    if token.endswith("x"):
        coefficient = token[:-1]

        if coefficient == "":
            return Variable("x")

        return BinaryOp(
            Value(float(coefficient)),
            "*",
            Variable("x")
        )

    return Value(float(token))

def parse_expression(expression):
    expression = expression.strip()

    if expression.startswith("(") and expression.endswith(")"):
        depth = 0
        enclosed = True

        for i, character in enumerate(expression):
            if character == "(":
                depth += 1
            elif character == ")":
                depth -= 1

            if depth == 0 and i != len(expression) - 1:
                enclosed = False
                break

        if enclosed:
            return parse_expression(expression[1:-1])

    operators = ["+", "-", "*", "/"]

    lowest_precedence = None
    operator_position = None
    depth = 0

    for i, character in enumerate(expression):
        if character == "(":
            depth += 1
        elif character == ")":
            depth -= 1
        elif character in operators and depth == 0:
            if character == "-" and (i == 0 or expression[i - 1] == "("):
                continue

            precedence = 1 if character in ("+", "-") else 2

            if lowest_precedence is None or precedence <= lowest_precedence:
                lowest_precedence = precedence
                operator_position = i

    if operator_position is None:
        return parse_token(expression)

    operator = expression[operator_position]
    left = expression[:operator_position]
    right = expression[operator_position + 1:]

    return BinaryOp(
        parse_expression(left),
        operator,
        parse_expression(right)
    )