def pytagoras_solver():
    from Calculator import calculator
    from Square_root_calculator import square_root
    What_should_be_calulated = input("Which should be calculated: a, b, c ")
    if What_should_be_calulated == "c":
        a = float(input(""))
        a = float(input("What is the adjacent cathetus(a) "))
        b = float(input("What is the opposite cathetus(b) "))
        a = calculator(a, "**", 2)
        b = calculator(b, "**", 2)
        c = calculator(a, "+", b)
        c = square_root(c, 2)
        print(f"c is {c}")
    elif What_should_be_calulated == "a":
        b = float(input("What is the opposite cathetus(b) "))
        c = float(input("What is the hypothenuse(c) "))
        b = calculator(b, "**", 2)
        c = calculator(c, "**", 2)
        a = calculator(c, "-", b)
        a = square_root(a,2)
        print(f"a is {a}")
    elif What_should_be_calulated == "b":
        a = float(input("What is the adjacent cathetus(a) "))
        c = float(input("What is the hypothenuse(c) "))
        a = calculator(a, "**", 2)
        c = calculator(c, "**", 2)
        b = calculator(c, "-", a)
        b = square_root(b, 2)
        print(f"b is {b}")