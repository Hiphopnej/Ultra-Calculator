from math import log, isfinite
from math import e as math_e
from ultra_calculator.text_functions import get_valid_input

def logarithm_calculator(value, base, shouldPrint=False, shouldAsk=False):
    # Creates a function for checking if the base is e
    def convert_base(base):
        if base.lower() == "e":
            return None
        return float(base)

    def convert_value(value):
        if isinstance(value, str) and value.lower() == "e":
            return math_e
        return float(value)

    if shouldAsk:
        # Makes sure value is above 0 because otherwise log will give an error
        value = get_valid_input(
            "What number do you want to calculate on? ",
            convert_value,
            lambda value: isfinite(value) and value > 0,
            "The number has to finite and be greater than 0."
        )

        # Makes sure base is e or above 1 because otherwise log will give an error
        base = get_valid_input(
            "What base do you want to use? (Enter e for natural logarithm): ",
            convert_base,
            lambda base: base is None or (isfinite(base) and base > 1),
            "Enter 'e' or a number greater than 1."
        )
    else:
        if isinstance(value, str):
            if value.lower() == "e":
                value = math_e
            else:
                raise TypeError("The number must be an integer, float, or 'e'.")
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("The number must be an integer or float.")

        if not isfinite(value) or value <= 0:
            raise ValueError("The number must be finite and greater than 0.")

        if base is not None:
            if isinstance(base, bool) or not isinstance(base, (int, float)):
                raise TypeError("The base must be an integer, float, or None.")

            if not isfinite(base) or base <= 1:
                raise ValueError("The base must be finite and greater than 1.")
            if (base-0.0000000000001) < 2.718281828459045 < (base+0.0000000000001):
                base = None
    if base is None: # If base is None that means no base should be used which log interprets as e
        result = log(value)
        if (value-0.0000000000001) < 2.718281828459045 < (value+0.0000000000001):
            value = "e"
        if shouldPrint:
            print(f"The logarithm of {value} with base e is {result}")
        return result
    else: # Otherwise use the base given by the user
        result = log(value, base)
        if (value-0.0000000000001) < 2.718281828459045 < (value+0.0000000000001):
            value = "e"
        if shouldPrint:
            print(f"The logarithm of {value} with base {base} is {result}")
        return result