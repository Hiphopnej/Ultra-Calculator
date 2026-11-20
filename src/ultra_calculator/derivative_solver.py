from ultra_calculator.equation_solver import Value, Variable, BinaryOp, Logarithm, Grouped, TrigonometricFunction, parse_expression
from ultra_calculator.simplify_equations import simplify

# Takes a function an returns the derivative of it
def derivative_solver(function=None, shouldPrint=False, shouldAsk=False):
    def finish(result):
        result = simplify(result)

        if shouldPrint:
            print(result.to_string())
        return result
    if shouldAsk:
        function = input("Enter an expression: ")

    if isinstance(function, str):
        while True:
            try:
                function = parse_expression(function)
                break
            except (ValueError, TypeError, SyntaxError):
                if not shouldAsk:
                    raise
                print("Invalid mathematical expression. Please try again.")
                function = input("Enter an expression: ")
    if isinstance(function, Value):
        return finish(Value(0))
    if isinstance(function, Variable):
        return finish(Value(1))
    if isinstance(function, Grouped):
        return finish(Grouped(derivative_solver(function.expression)))
    if isinstance(function, Logarithm):
        if function.base is None:
            return finish(BinaryOp(derivative_solver(function.value), "/", function.value))
        else:
            return finish(BinaryOp(derivative_solver(function.value), "/", BinaryOp(Grouped(function.value) if isinstance(function.value, BinaryOp) else function.value, "*", Logarithm(function.base))))
    if isinstance(function, TrigonometricFunction):
        if function.function == "sin":
            return finish(BinaryOp(TrigonometricFunction("cos", function.value), "*", derivative_solver(function.value)))
        elif function.function == "cos":
            return finish(BinaryOp(BinaryOp(Value(-1), "*", TrigonometricFunction("sin", function.value)), "*", derivative_solver(function.value)))
        elif function.function == "tan":
            return finish(BinaryOp(BinaryOp(Value(1), "/", BinaryOp(TrigonometricFunction("cos", function.value), "^", Value(2))), "*", derivative_solver(function.value)))
    if isinstance(function, BinaryOp):
        if function.operator == "+":
            return finish(BinaryOp(derivative_solver(function.left), "+", derivative_solver(function.right)))
        if function.operator == "-":
            return finish(BinaryOp(derivative_solver(function.left), "-", derivative_solver(function.right)))
        if function.operator == "*":
            return finish(BinaryOp(BinaryOp(derivative_solver(function.left), "*", function.right), "+", BinaryOp(function.left, "*", derivative_solver(function.right))))
        if function.operator == "/":
            return finish(BinaryOp(BinaryOp(BinaryOp(derivative_solver(function.left), "*", function.right), "-", BinaryOp(function.left, "*", derivative_solver(function.right))), "/", BinaryOp(function.right, "*", function.right)))
        if function.operator == "^":
            if isinstance(function.right, Value):
                return finish(BinaryOp(BinaryOp(function.right, "*", BinaryOp(function.left, "^", Value(function.right.value-1))), "*", derivative_solver(function.left)))
            elif isinstance(function.right, Variable):
                return finish(BinaryOp(function, "*", Logarithm(function.left)))
            elif isinstance(function.right, BinaryOp):
                return finish(BinaryOp(BinaryOp(function, "*", Logarithm(function.left)), "*", derivative_solver(function.right)))
        raise ValueError(f"Unsupported operator: {function.operator}")
    raise ValueError("Unsupported expression")