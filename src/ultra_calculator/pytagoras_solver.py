from ultra_calculator.calculator import calculator
from ultra_calculator.square_root_calculator import square_root

def pytagoras_solver(side, a=None, b=None, c=None, shouldPrint=False, shouldAsk=False):
    if shouldAsk:
        side = input("Which should be calculated: a, b, c ")
    if side == "c":
        if shouldAsk:
            a = float(input("What is the adjacent cathetus(a) "))
            b = float(input("What is the opposite cathetus(b) "))
        a = calculator(a, "**", 2)
        b = calculator(b, "**", 2)
        c = calculator(a, "+", b)
        c = square_root(c, 2)
        if shouldPrint:
            print(f"c is {c}")
        return c
    elif side == "a":
        if shouldAsk:
            b = float(input("What is the opposite cathetus(b) "))
            c = float(input("What is the hypothenuse(c) "))
        b = calculator(b, "**", 2)
        c = calculator(c, "**", 2)
        a = calculator(c, "-", b)
        a = square_root(a,2)
        if shouldPrint:
            print(f"a is {a}")
        return a
    elif side == "b":
        if shouldAsk:
            a = float(input("What is the adjacent cathetus(a) "))
            c = float(input("What is the hypothenuse(c) "))
        a = calculator(a, "**", 2)
        c = calculator(c, "**", 2)
        b = calculator(c, "-", a)
        b = square_root(b, 2)
        if shouldPrint:
            print(f"b is {b}")
        return b
    else:
        raise ValueError("Invalid side")