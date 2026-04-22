from Calculator import calculator

choices = ["calculator"]
file_choice = input(f"What to you want to calulate. Options: {choices} ")

if file_choice.lower() == "calculator":
    calculator(0,"",0,True,True)