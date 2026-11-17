from ultra_calculator.equation_solver import Value, Variable, BinaryOp

# Takes a function an returns the derivative of it
def derivative_solver(function, shouldPrint=False, shouldAsk=False):
    if isinstance(function, Value):
        return Value(0)
    if isinstance(function, Variable):
        return Value(1)
    if isinstance(function, BinaryOp):
        if function.operator == "+":
            return BinaryOp(derivative_solver(function.left), "+", derivative_solver(function.right))
        if function.operator == "-":
            return BinaryOp(derivative_solver(function.left), "-", derivative_solver(function.right))
        if function.operator == "*":
            return BinaryOp(BinaryOp(derivative_solver(function.left), "*", function.right), "+", BinaryOp(function.left, "*", derivative_solver(function.right)))
        if function.operator == "/":
            return BinaryOp(BinaryOp(BinaryOp(derivative_solver(function.left), "*", function.right), "-", BinaryOp(function.left, "*", derivative_solver(function.right))), "/", BinaryOp(function.right, "*", function.right))

        raise ValueError("Unsupported expression")