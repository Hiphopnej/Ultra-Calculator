from Calculator import calculator
from Square_root_calculator import square_root
from Pq_solver import pq_solver
from Pytagoras_solver import pytagoras_solver
from Shape_solver import shape_solver

choices = ["calculator", "square root", "pq solver", "pytagoras solver", "shape solver"]
file_choice = input(f"What to you want to calulate. Options: {choices} ")

if file_choice.lower() == "calculator":
    calculator(0,"",0,True,True)
elif file_choice == "square root":
    square_root(0,0, True, True)
elif file_choice == "pq solver":
    pq_solver()
elif file_choice == "pytagoras solver":
    pytagoras_solver()
elif file_choice == "shape solver":
    shape_solver()