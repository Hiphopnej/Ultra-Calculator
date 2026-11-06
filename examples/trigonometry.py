from ultra_calculator.trigonometry_calculator import trigonometry
import math

# Calculates the sine of 90 degrees. 
# Expected output is: The sine of 90 in degrees is 1.0
trigonometry("sin",90,"degrees", True)

# Calculates the arccosine in degrees of 0. 
# Expected output is: The arccos of 0 in degrees is 90.0
trigonometry("arccos", 0, "degrees", True)

# Calculates the tangent of pi radians. 
# Expected output is: The tangent of 3.141592653589793 in radians is 0.0
trigonometry("tan", math.pi, "radians", True)

# Calculate the arctangent in tangent of 0. 
# Expected output is: The arctan of 0 in radians is 0.0
trigonometry("arctan", 0, "radians", True)

# Asks for function(sin, cos...), degrees or radians and number, 
# calculates it and prints it out
trigonometry(None, None, None, True, True)