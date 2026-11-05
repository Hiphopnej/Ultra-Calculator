from ultra_calculator.text_functions import inquirer_input, get_valid_input
import math

def trigonometry(function, value, radians_or_degrees, shouldPrint=False, shouldAsk=False):
    # Adds the varible ROUNDING for how many decimal everything should be round to.
    # This is to avoid the impreciseness of float.
    ROUNDING = 10
    if shouldAsk:
        function = inquirer_input("What do you want to calculate?", ["Sin", "Cos", "Tan", "Arcsin", "Arccos", "Arctan"])
        radians_or_degrees = inquirer_input("", ["Radians", "Degrees"])

        if function.lower() in ["arcsin", "arccos"]:
            value = get_valid_input(
                "What number do you want to calculate on? ",
                float,
                lambda value: -1 <= value <= 1,
                "The value must be between -1 and 1."
            )
        else:
            value = get_valid_input(
                "What number do you want to calculate on? ",
                float
            )

    if function.lower() not in ["sin", "cos", "tan", "arcsin", "arccos", "arctan"]:
            raise ValueError("Invalid trigonometric function")
    
    if radians_or_degrees.lower() not in ["radians", "degrees"]:
        raise ValueError("Invalid angle unit")
    
    if function.lower() == "sin":
        if radians_or_degrees.lower() == "radians":
            answer = round(math.sin(value), ROUNDING)
            if shouldPrint:
                print(f"The sine of {value} in radians is {answer}")
            return answer
        elif radians_or_degrees.lower() == "degrees":
            # If you multiply a value in degrees with pi/180 you get it in radians
            answer = round(math.sin(value*(math.pi/180)), ROUNDING)
            if shouldPrint:
                print(f"The sine of {value} in degrees is {answer}")
            return answer
    elif function.lower() == "cos":
        if radians_or_degrees.lower() == "radians":
            answer = round(math.cos(value), ROUNDING)
            if shouldPrint:
                print(f"The cosine of {value} in radians is {answer}")
            return answer
        elif radians_or_degrees.lower() == "degrees":
            answer = round(math.cos(value*(math.pi/180)), ROUNDING)
            if shouldPrint:
                print(f"The cosine of {value} in degrees is {answer}")
            return answer
    elif function.lower() == "tan":
        if radians_or_degrees.lower() == "radians":
            answer = round(math.tan(value), ROUNDING)
            if shouldPrint:
                print(f"The tangent of {value} in radians is {answer}")
            return answer
        elif radians_or_degrees.lower() == "degrees":
            answer = round(math.tan(value*(math.pi/180)), ROUNDING)
            if shouldPrint:
                print(f"The tangent of {value} in degrees is {answer}")
            return answer
    elif function.lower() == "arcsin":
        if radians_or_degrees.lower() == "radians":
            answer = round(math.asin(value), ROUNDING)
            if shouldPrint:
                print(f"The arcsine of {value} in radians is {answer}")
            return answer
        elif radians_or_degrees.lower() == "degrees":
            answer = round((math.asin(value)*(180/math.pi)), ROUNDING)
            if shouldPrint:
                print(f"The arcsine of {value} in degrees is {answer}")
            return answer
    elif function.lower() == "arccos":
        if radians_or_degrees.lower() == "radians":
            answer = round(math.acos(value), ROUNDING)
            if shouldPrint:
                print(f"The arccos of {value} in radians is {answer}")
            return answer
        elif radians_or_degrees.lower() == "degrees":
            answer = round((math.acos(value)*(180/math.pi)), ROUNDING)
            if shouldPrint:
                print(f"The arccos of {value} in degrees is {answer}")
            return answer
    elif function.lower() == "arctan":
        if radians_or_degrees.lower() == "radians":
            answer = round(math.atan(value), ROUNDING)
            if shouldPrint:
                print(f"The arctan of {value} in radians is {answer}")
            return answer
        elif radians_or_degrees.lower() == "degrees":
            answer = round((math.atan(value)*(180/math.pi)), ROUNDING)
            if shouldPrint:
                print(f"The arctan of {value} in degrees is {answer}")
            return answer