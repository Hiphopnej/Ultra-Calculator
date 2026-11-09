from math import log
from ultra_calculator.text_functions import get_valid_input

def logarithm_calculator(value, base, shouldPrint, shouldAsk):
    # Creates a function for checking if the base is e
    def convert_base(base):
        if base.lower() == "e":
            return None
        return int(base)

    if shouldAsk:
        # Makes sure value is above 0 because otherwise log will give an error
        value = get_valid_input(
            "What number do you want to calculate on? ",
            float,
            lambda value: value > 0,
            "The number has to be greater than 0."
        )

        # Makes sure base is e or above 1 because otherwise log will give an error
        base = get_valid_input(
            "What base do you want to use? (Enter e for natural logarithm): ",
            convert_base,
            lambda base: base is None or base >= 2,
            "Enter 'e' or an integer greater than 1."
        )
    if base == None: # If base is None that means no base should be used which log interprets as e
        result = log(value)
        if shouldPrint:
            print(f"The logarithm of {value} with base e is {result}")
        return result
    else: # Otherwise use the base given by the user
        result = log(value, base)
        if shouldPrint:
            print(f"The logarithm of {value} with base {base} is {result}")