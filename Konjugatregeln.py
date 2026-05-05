from Kvadreringsregeln import parse_term
from Kvadreringsregeln import add_term
from Kvadreringsregeln import format_polynomial

def konjugatregeln(number1, number2, shouldPrint=False, shouldAsk=False):

    if shouldAsk:
        number1 = input("What is your first term: ")
        number2 = input("What is your second term: ")
    
    result = fix_num(number1, number2)

    if shouldPrint:
        print(result)

    return result

def fix_num(number1, number2):
    a_coeff, a_exp = parse_term(number1)
    b_coeff, b_exp = parse_term(number2)

    terms = {}

    # a^2
    add_term(terms, a_coeff ** 2, a_exp * 2)

    # - b^2
    add_term(terms, -(b_coeff ** 2), b_exp * 2)

    return format_polynomial(terms)