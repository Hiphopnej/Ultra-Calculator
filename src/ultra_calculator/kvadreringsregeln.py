def kvadreringsregeln(number1, number2, plus_or_minus, shouldPrint=False, shouldAsk=False):
    if shouldAsk:
        number1 = input("What is your first term: ")
        number2 = input("What is your second term: ")
        plus_or_minus = input("Choose + or - ")

    if plus_or_minus not in ("+", "-"):
        raise ValueError("Operator must be '+' or '-'")

    result = fix_num(number1, number2, plus_or_minus)

    if shouldPrint:
        print(result)

    return result

def parse_term(term):
    term = term.replace(" ", "")
    term = term.replace("^", "**")

    if "x" not in term:
        return int(term), 0

    coeff = 1
    exponent = 1

    parts = term.split("x")

    if parts[0] not in ("", "+"):
        if parts[0] == "-":
            coeff = -1
        else:
            coeff = int(parts[0])

    if "**" in term:
        exponent = int(term.split("**")[1])

    return coeff, exponent

def add_term(terms, coefficient, exp):
    if exp in terms:
        terms[exp] += coefficient
    else:
        terms[exp] = coefficient

def format_polynomial(terms):
    sorted_terms = sorted(terms.items(), key=lambda x: -x[0])
    result = ""

    for exp, coefficient in sorted_terms:
        if coefficient == 0:
            continue

        if result == "":
            sign = "-" if coefficient < 0 else ""
        else:
            sign = "+" if coefficient > 0 else "-"

        coefficient_abs = abs(coefficient)

        if exp == 0:
            term = f"{coefficient_abs}"
        elif exp == 1:
            term = "x" if coefficient_abs == 1 else f"{coefficient_abs}x"
        else:
            term = f"x^{exp}" if coefficient_abs == 1 else f"{coefficient_abs}x^{exp}"

        result += sign + term

    return result if result else "0"

def fix_num(number1, number2, plus_or_minus):
    a_coefficient, a_exp = parse_term(number1)
    b_coefficient, b_exp = parse_term(number2)

    terms = {}

    add_term(terms, a_coefficient ** 2, a_exp * 2)

    middle_coefficient = 2 * a_coefficient * b_coefficient

    if plus_or_minus == "-":
        middle_coefficient *= -1

    add_term(terms, middle_coefficient, a_exp + b_exp)

    add_term(terms, b_coefficient ** 2, b_exp * 2)

    return format_polynomial(terms)