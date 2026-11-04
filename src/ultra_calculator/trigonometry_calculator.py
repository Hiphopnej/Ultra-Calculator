from ultra_calculator.text_functions import inquirer_input
import math

def trigonometry(function, value, radians_or_degrees, shouldPrint, shouldAsk):
    ROUNDING = 10
    if shouldAsk:
        function = inquirer_input("What do you want to calculate?", ["Sin", "Cos", "Tan", "Arcsin", "Arccos", "Arctan"])
        value = float(input("What number do you want to cacluate on? "))
        radians_or_degrees = inquirer_input("", ["Radians", "Degrees"])
    
    if function.lower() == "sin":
        if radians_or_degrees.lower() == "radians":
            answer = round(math.sin(value), ROUNDING)
            if shouldPrint:
                print(f"The sine of {value} in radians is {answer}")
            return answer
        elif radians_or_degrees.lower() == "degrees":
            answer = round(math.sin(value*(math.pi/180)), ROUNDING)
            if shouldPrint:
                print(f"The sine of {value} in radians is {answer}")
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