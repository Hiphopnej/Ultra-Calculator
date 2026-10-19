from ultra_calculator.calculator import calculator

def square_root(number, root, shouldPrint=False, shouldAsk=False):
    if shouldAsk:
        root = float(input("Which root do want to use? "))
        number = float(input("What number to you want to root? "))
    answer = calculator(number, "**", calculator(1, "/", root))
    if shouldPrint:
        print(f"The {root} root of {number} is: {answer}")
    return answer