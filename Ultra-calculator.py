from Calculator import calculator
from Square_root_calculator import square_root

choices = ["calculator", "square root"]
file_choice = input(f"What to you want to calulate. Options: {choices} ")

if file_choice.lower() == "calculator":
    calculator(0,"",0,True,True)
elif file_choice == "square root":
    square_root(0,0, True, True)