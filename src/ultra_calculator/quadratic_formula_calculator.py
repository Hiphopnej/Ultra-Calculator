from ultra_calculator.text_functions import get_valid_input
from cmath import sqrt

def quadratic_formula_calculator(a, b, c, shouldPrint=False, shouldAsk=False):
    def format_complex(z):
        real = z.real
        imag = z.imag

        # If purely real
        if imag == 0:
            return f"{real}"

        # If purely imaginary
        if real == 0:
            return f"{imag}i"

        # Full complex number
        sign = '+' if imag >= 0 else '-'
        return f"{real} {sign} {abs(imag)}i"
    def convert_complex(value):
        return complex(value.replace("i", "j"))
    if shouldAsk:
        a = get_valid_input(
            "What is a? ",
            convert_complex,
            lambda value: value != 0,
            "Answer has to be a number and not zero"
        )
        b = get_valid_input(    
            "What is b? ",
            convert_complex,
            None,
            "Answer has to be a number"
        )
        c = get_valid_input(
            "What is c? ",
            convert_complex,
            None,
            "Answer has to be a number"
        )

    denominator = 2*a
    numerator_root = sqrt((b**2)-(4*a*c))
    if numerator_root == 0:
        x1 = (-b)/denominator
        x2 = None
        if shouldPrint:
            print(f"x = {format_complex(x1)}")
        return x1, x2
    else:
        x1 = (-b+(numerator_root))/denominator
        x2 = (-b-(numerator_root))/denominator
        if shouldPrint:
            print(f"x1 = {format_complex(x1)}")
            print(f"x2 = {format_complex(x2)}")
        return x1, x2