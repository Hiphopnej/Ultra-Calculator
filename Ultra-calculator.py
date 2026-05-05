from Calculator import calculator
from Square_root_calculator import square_root
from Pq_solver import pq_solver
from Pytagoras_solver import pytagoras_solver
from Shape_solver import shape_solver
from Kvadreringsregeln import kvadreringsregeln
from Konjugatregeln import konjugatregeln
from InquirerPy import inquirer

def inquirer_input(message_param, options):
    choice = inquirer.select(
        message=message_param,
        choices = options
    ).execute()
    return choice


choices = ["calculator", "square root", "pq solver", "pytagoras solver", "shape solver", "kvadreringsregeln", "konjugatregeln"]
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
    kvadreringsregeln(0,0, "", True, True)
elif file_choice == "konjugatregeln":
    konjugatregeln(0,0, True, True)