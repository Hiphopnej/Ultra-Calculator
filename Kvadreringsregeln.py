def kvadreringsregeln(number1, number2, plus_or_minus, shouldPrint=True, shouldAsk=False):
    if shouldAsk:
        number1 = input("What is your first term: ")
        number2 = input("What is your second term: ")

    result = fix_num(number1, number2, plus_or_minus)

    if shouldPrint:
        print(result)

    return result

def parse_term(term):
    term = term.replace(" ", "")

    # If there is no x
    if "x" not in term:
        return int(term), 0

    # Split coefficient and x-part
    if "*" in term:
        parts = term.split("*")
        # Makes sure making parts[0] an int doesn't give an error
        if parts[0] == "" or parts[0] == "x":
            coeff = 1
        else:
            coeff = int(parts[0])
        x_part = parts[1]
    else:
        # Handle "3x**2" or "x**2"
        if term.startswith("x"):
            coeff = 1
            x_part = term
        else:
            coeff = int(term.split("x")[0])
            x_part = term[len(str(coeff)):]

    # Extract exponent
    if "**" in x_part:
        exponent = int(x_part.split("**")[1])
    else:
        exponent = 1

    return coeff, exponent

def add_term(terms, coefficient, exp):
        if exp in terms:
            terms[exp] += coefficient
        else:
            terms[exp] = coefficient

def format_polynomial(terms):
        # Sort by exponent descending
        sorted_terms = sorted(terms.items(), key=lambda x: -x[0])

        result = ""
        for exp, coefficient in sorted_terms:
            if coefficient == 0:
                continue

            # Sign handling
            if result == "":
                sign = "-" if coefficient < 0 else ""
            else:
                sign = "+" if coefficient > 0 else "-"

            coefficient_abs = abs(coefficient)

            # Formatting term
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

        # a^2
        add_term(terms, a_coefficient ** 2, a_exp * 2)

        # +-2ab
        middle_coefficient = 2 * a_coefficient * b_coefficient
        if plus_or_minus == "-":
            middle_coefficient *= -1
        add_term(terms, middle_coefficient, a_exp + b_exp)

        # b^2
        add_term(terms, b_coefficient ** 2, b_exp * 2)

        return format_polynomial(terms)