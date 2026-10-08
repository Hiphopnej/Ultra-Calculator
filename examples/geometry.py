from ultra_calculator.shape_solver import shape_solver

# Calculate area for a triangle with base 10 and height 5. The expected output is 25.0
shape_solver("2D","Triangle", True, base=10,height=5)

# Calculate the volume and the surface area of a sphere with radius 3. The expected output for both is approximetly 113.097
shape_solver("3D","Sphere", True, radius=3)