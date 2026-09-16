from ultra_calculator.calculator import calculator
from ultra_calculator.square_root_calculator import square_root
from ultra_calculator.pq_solver import pq_solver
from ultra_calculator.pytagoras_solver import pytagoras_solver
from ultra_calculator.shape_solver import shape_solver
from ultra_calculator.kvadreringsregeln import kvadreringsregeln
from ultra_calculator.konjugatregeln import konjugatregeln
from ultra_calculator.equation_solver import equation_solver
from InquirerPy import inquirer

def inquirer_input(message_param, options):
    choice = inquirer.select(
        message=message_param,
        choices = options
    ).execute()
    return choice


choices = [
    "calculator", 
    "square root", 
    "pq solver", 
    "pytagoras solver", 
    "shape solver", 
    "kvadreringsregeln", 
    "konjugatregeln", 
    "equation solver"
    ]
file_choice = inquirer_input("What do you want to calculate", choices)

if file_choice == "calculator":
    calculator(0,"",0,True,True)
elif file_choice == "square root":
    square_root(0,0, True, True)
elif file_choice == "pq solver":
    pq_solver()
elif file_choice == "pytagoras solver":
    pytagoras_solver()
elif file_choice == "shape solver":
    shape_solver()
elif file_choice == "kvadreringsregeln":
    kvadreringsregeln(None,None,None,True,True)
elif file_choice == "konjugatregeln":
    konjugatregeln(0,0, True, True)
elif file_choice == "equation solver":
    equation_solver(True)