from Calculator import calculator
from Square_root_calculator import square_root
from Pq_solver import pq_solver

choices = ["calculator", "square root", "pq solver"]
file_choice = input(f"What to you want to calulate. Options: {choices} ")

if file_choice.lower() == "calculator":
    calculator(0,"",0,True,True)
elif file_choice == "square root":
    square_root(0,0, True, True)
elif file_choice == "pq solver":
    pq_solver()