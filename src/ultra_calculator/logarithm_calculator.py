from math import log, isfinite
from ultra_calculator.text_functions import get_valid_input

def logarithm_calculator(value, base, shouldPrint, shouldAsk):
    # Creates a function for checking if the base is e
    def convert_base(base):
        if base.lower() == "e":
            return None
        return float(base)

    if shouldAsk:
        # Makes sure value is above 0 because otherwise log will give an error
        value = get_valid_input(
            "What number do you want to calculate on? ",
            float,
            lambda value: isfinite(value) and value > 0,
            "The number has to be greater than 0."
        )

        # Makes sure base is e or above 1 because otherwise log will give an error
        base = get_valid_input(
            "What base do you want to use? (Enter e for natural logarithm): ",
            convert_base,
            lambda base: base is None or (isfinite(base) and base > 1),
            "Enter 'e' or a number greater than 1."
        )
    else:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("The number must be an integer or float.")

        if not isfinite(value) or value <= 0:
            raise ValueError("The number must be finite and greater than 0.")

        if base is not None:
            if isinstance(base, bool) or not isinstance(base, (int, float)):
                raise TypeError("The base must be an integer, float, or None.")

            if not isfinite(base) or base <= 1:
                raise ValueError("The base must be finite and greater than 1.")
    if base is None: # If base is None that means no base should be used which log interprets as e
        result = log(value)
        if shouldPrint:
            print(f"The logarithm of {value} with base e is {result}")
        return result
    else: # Otherwise use the base given by the user
        result = log(value, base)
        if shouldPrint:
            print(f"The logarithm of {value} with base {base} is {result}")
        return result