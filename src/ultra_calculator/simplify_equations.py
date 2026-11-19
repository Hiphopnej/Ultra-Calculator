from ultra_calculator.equation_solver import Value, Variable, Grouped, TrigonometricFunction, Logarithm, BinaryOp

def simplify(function):
    if isinstance(function, (Value, Variable)):
        return function

    if isinstance(function, Grouped):
        return Grouped(simplify(function.expression))

    if isinstance(function, TrigonometricFunction):
        return TrigonometricFunction(function.function, simplify(function.value))

    if isinstance(function, Logarithm):
        base = simplify(function.base) if function.base is not None else None
        return Logarithm(simplify(function.value), base)

    if isinstance(function, BinaryOp):
        left = simplify(function.left)
        right = simplify(function.right)

        if isinstance(left, Value) and isinstance(right, Value):
            try:
                if function.operator == "+":
                    return Value(left.value + right.value)
                if function.operator == "-":
                    return Value(left.value - right.value)
                if function.operator == "*":
                    return Value(left.value * right.value)
                if function.operator == "/":
                    return Value(left.value / right.value)
                if function.operator == "^":
                    result = left.value ** right.value
                    if isinstance(result, complex):
                        return BinaryOp(left, function.operator, right)
                    return Value(result)
            except (ZeroDivisionError, ValueError, OverflowError):
                pass

        if function.operator == "+":
            if isinstance(left, Value) and left.value == 0:
                return right
            if isinstance(right, Value) and right.value == 0:
                return left

        if function.operator == "-":
            if isinstance(right, Value) and right.value == 0:
                return left

        if function.operator == "*":
            if isinstance(left, Value) and left.value == 0:
                return Value(0)
            if isinstance(right, Value) and right.value == 0:
                return Value(0)
            if isinstance(left, Value) and left.value == 1:
                return right
            if isinstance(right, Value) and right.value == 1:
                return left

        if function.operator == "/":
            if isinstance(left, Value) and left.value == 0:
                return Value(0)
            if isinstance(right, Value) and right.value == 1:
                return left

        if function.operator == "^":
            if isinstance(right, Value) and right.value == 0:
                return Value(1)
            if isinstance(right, Value) and right.value == 1:
                return left

        return BinaryOp(left, function.operator, right)