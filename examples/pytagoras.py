from ultra_calculator.pytagoras_solver import pytagoras_solver

# Calculates pytagoras theorem for the side c with side a and b being 20 and 5 respectivly and prints it out.
# Expected output is: c is 20.615528128088304
pytagoras_solver("c", 20, 5, None, True)

# Asks what side you want to calculate and the length of the other side and then calculates the length of the side you want using pytagoras theorem.
pytagoras_solver(None, None, None, None, True, True)