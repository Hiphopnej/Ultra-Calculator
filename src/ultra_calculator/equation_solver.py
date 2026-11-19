from math import e as math_e

class Node:
    def to_string(self):
        raise NotImplementedError

class Value(Node):
    def __init__(self, value, symbol=None):
        self.value = value
        self.symbol = symbol

    def to_string(self):
        if self.symbol is not None:
            return self.symbol
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
        if self.operator == "^":
            return 3
        return 0

    def to_string(self):
        left = self.left.to_string()
        right = self.right.to_string()

        if isinstance(self.left, BinaryOp) and (self.left.precedence() < self.precedence() or (self.operator == "^" and self.left.operator == "^")):
            left = f"({left})"

        if isinstance(self.right, BinaryOp) and (self.right.precedence() < self.precedence() or (self.operator == "-" and self.right.operator in ("+", "-")) or (self.operator == "/" and self.right.operator in ("*", "/")) or (self.operator == "*" and self.right.operator in ("*", "/"))):
            right = f"({right})"

        return f"{left} {self.operator} {right}"

class Logarithm(Node):
    def __init__(self, value, base=None):
        self.value = value
        self.base = base

    def to_string(self):
        if self.base is None:
            return f"ln({self.value.to_string()})"

        return f"log({self.value.to_string()}, {self.base.to_string()})"

class Grouped(Node):
    def __init__(self, expression):
        self.expression = expression

    def to_string(self):
        return f"({self.expression.to_string()})"

class Equation:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def to_string(self):
        return f"{self.left.to_string()} = {self.right.to_string()}"

def parse_token(token):
    token = token.strip()

    if token == "-x":
        return BinaryOp(
            Value(-1),
            "*",
            Variable("x")
        )

    if token.startswith("ln(") and token.endswith(")"):
        expression = token[3:-1]
        parsed_expression = parse_expression(expression)
        return Logarithm(parsed_expression)

    if token.startswith("log(") and token.endswith(")"):
        expression = token[4:-1]
        counter = 0
        if "," not in expression:
            raise ValueError(", has to be used to separate value and base")
        
        for i, char in enumerate(expression):
            if char == "(":
                counter += 1
            if char == ")":
                counter -= 1
            if char == "," and counter == 0:
                comma_index = i
                break

        value = expression[:comma_index].strip()
        base = expression[comma_index+1:].strip()

        if not base:
            raise ValueError("A logarithm must have a base")

        parsed_value = parse_expression(value)
        parsed_base = parse_expression(base)

        if not isinstance(parsed_base, Value):
            raise ValueError("The logarithm base must be a numeric constant")

        if parsed_base.value <= 0 or parsed_base.value == 1:
            raise ValueError("The logarithm base must be positive and cannot be 1")

        return Logarithm(parsed_value, parsed_base)
                

    if token.endswith("x"):
        coefficient = token[:-1]

        if coefficient == "":
            return Variable("x")

        return BinaryOp(
            Value(float(coefficient)),
            "*",
            Variable("x")
        )
    if token == "e":
        return Value(math_e, "e")

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

    operators = ["+", "-", "*", "/", "^"]

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

            precedence = 3 if character == "^" else (1 if character in ("+", "-") else 2)

            if lowest_precedence is None or precedence < lowest_precedence:
                lowest_precedence = precedence
                operator_position = i
            elif precedence == lowest_precedence and character != "^":
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

def parse_equation(equation):
    equation = equation.strip()

    if equation.count("=") != 1:
        raise ValueError("An equation must contain exactly one '='.")

    left, right = equation.split("=")

    return Equation(
        parse_expression(left),
        parse_expression(right)
    )

def linear_form(node):
    if isinstance(node, Value):
        return 0, node.value

    if isinstance(node, Variable):
        return 1, 0

    if isinstance(node, BinaryOp):
        left_coefficient, left_constant = linear_form(node.left)
        right_coefficient, right_constant = linear_form(node.right)

        if node.operator == "+":
            return (
                left_coefficient + right_coefficient,
                left_constant + right_constant
            )

        if node.operator == "-":
            return (
                left_coefficient - right_coefficient,
                left_constant - right_constant
            )

        if node.operator == "*":
            if left_coefficient != 0 and right_coefficient != 0:
                raise ValueError("Non-linear expression")

            if left_coefficient != 0:
                return (
                    left_coefficient * right_constant,
                    left_constant * right_constant
                )

            if right_coefficient != 0:
                return (
                    right_coefficient * left_constant,
                    right_constant * left_constant
                )

            return 0, left_constant * right_constant

        if node.operator == "/":
            if right_coefficient != 0:
                raise ValueError("Cannot divide by an expression containing x")

            if right_constant == 0:
                raise ValueError("Division by zero")

            return (
                left_coefficient / right_constant,
                left_constant / right_constant
            )

    raise ValueError("Unsupported expression")

def solve_equation(equation):
    left_coefficient, left_constant = linear_form(equation.left)
    right_coefficient, right_constant = linear_form(equation.right)

    coefficient = left_coefficient - right_coefficient
    constant = right_constant - left_constant

    if coefficient == 0:
        if constant == 0:
            raise ValueError("The equation has infinitely many solutions")

        raise ValueError("The equation has no solution")

    return constant / coefficient

def equation_solver(equation=None, shouldPrint=False, shouldAsk=False):
    if shouldAsk:
        equation = input("Enter an equation: ")

    try:
        result = solve_equation(parse_equation(equation))
        if shouldPrint:
            print(f"x = {result}")
            return result
        else:
            return result
    except ValueError as e:
        print(f"Error: {e}")