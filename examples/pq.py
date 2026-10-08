from ultra_calculator.pq_solver import pq_solver

# Prints the x values if p is -5 and q is 6. Expected output is:
# x1 = 3.0 
# and 
# x2 = 2.0
pq_solver(-5, 6, True)

# Complex example. Expected output is: 
# x1 = -1.0 + 2.0i 
# and 
# x2 = -1.0 - 2.0i
pq_solver(2, 5, True)