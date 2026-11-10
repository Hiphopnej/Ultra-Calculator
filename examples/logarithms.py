from ultra_calculator.logarithm_calculator import logarithm_calculator
from math import e

# Calculates the logarithm of 7 with base 5 and prints it out. 
# Expected output is: The logarithm of 7 with base 5 is 1.2090619551221675
logarithm_calculator(7, 5, True)

# Calculates the logarithm of 2.14 with base 11.3 and prints it out. 
# Expected output is: The logarithm of 2.14 with base 11.3 is 0.3137598869237447
logarithm_calculator(2.14, 11.3, True)

# Calculates the logarithm of 5 with base e and prints it out. 
# Expected output is: The logarithm of 5 with base 2.718281828459045 is 1.6094379124341003
logarithm_calculator(5, e, True)

# Asks for number and base and calculates the logarithm with that base
logarithm_calculator(None, None, True, True)