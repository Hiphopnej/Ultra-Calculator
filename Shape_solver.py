def shape_solver():
    #Gör ett program som räknar ut area och även mantelarean och Omkretsen för vissa former där det är svårt att räkna ut
    import math
    from Calculator import calculator
    from Square_root_calculator import square_root
    #Asks what type of shape you want to calculate
    TwoD_or_ThreeD = input("Do you want to calculate shapes in 2D or 3D ")
    Shapes3d = ["Cuboid", "Prism", "Cylinder", "Pyramid", "Cone", "Sphere"]
    Shapes2d = ["Triangle", "Rectangle", "Parallellogram", "Parallel_trapezoid", "Circle"]
    #Ask what shape you want to calculate
    if TwoD_or_ThreeD == "3D":
        Shape3d = input(f"Which of these shapes whould you like to calculate:{Shapes3d} ")
        #Checks which 3d shape to calculate
        if Shape3d == "Cuboid":
            Base_surface = input("What is the base surface of the object ")
            Height = input("What is the height of the object ")
            Volume = calculator(float(Base_surface), "*", float(Height))
            print(f"For a {Shape3d} with the base surface of {Base_surface} and height of {Height} the volume is {Volume}")

        elif Shape3d == "Prism":
            Base_surface = input("What is the base surface of the object ")
            Height = input("What is the height of the object ")
            Volume = calculator(float(Base_surface), "*", float(Height))
            print(f"For a {Shape3d} with the base surface of {Base_surface} and height of {Height} the volume is {Volume}")

        elif Shape3d == "Cylinder":
            radius = input("What is the radius of the base surface ")
            Base_surface = input("What is the base surface of the object ")
            Height = input("What is the height of the object ")
            Volume = calculator(float(Base_surface), "*", float(Height))
            print(f"For a {Shape3d} with the base surface of {Base_surface} and height of {Height} the volume is {Volume}")
            mantlearea = 2 * float(math.pi) * float(radius) * float(Height)
            print(f"The mantel area of the cylinder is {mantlearea}")

        elif Shape3d == "Pyramid":
            Base_surface = input("What is the base surface of the object ")
            Height = input("What is the height of the object ")
            Volume = calculator(calculator(float(Base_surface), "*", float(Height)), "/", 3)
            print(f"For a {Shape3d} with the base surface of {Base_surface} and height of {Height} the volume is {Volume}")

        elif Shape3d == "Cone":
            Base_surface = input("What is the base surface of the object ")
            Height = input("What is the height of the object ")
            Volume = calculator(calculator(float(Base_surface), "*", float(Height)), "/", 3)
            radius = input("What is the radius of the base surface ")
            Produkt1 = calculator(float(radius), "*", float(radius))
            Produkt2 = calculator(float(Height), "**", 2)
            slope = square_root(calculator(Produkt1, "+", Produkt2), 2)
            Mantlearea = calculator(calculator(float(math.pi), "*", float(radius)), "*", float(slope))
            print(f"For a {Shape3d} with the base surface of {Base_surface} and height of {Height} the volume is {Volume}")
            print(f"The Mantle area is {Mantlearea}")

        elif Shape3d == "Sphere":
            radius = input("What is the radius of the object ")
            Produkt = calculator(calculator(math.pi, "*", 4), "*", calculator(float(radius), "**", 3))
            Volume = calculator(Produkt, "/", 3)
            print(f"If the radius of the sphere is {radius} then the volume is {Volume}")
            Area = calculator(calculator(math.pi, "*", 4), "*", calculator(float(radius), "**", 2))
            print(f"The area of the sphere is {Area}")
    elif TwoD_or_ThreeD == "2D":
        Shape2d = input(f"Which of these shapes whould you like to calculate:{Shapes2d} ")
        #Checks what 2d shape to calculate
        if Shape2d == "Triangle":
            Base = input("What is the base of the object ")
            Height = input("What is the height of the object ")
            Produkt1 = calculator(float(Base), "*", float(Height))
            Area = calculator(Produkt1, "/", 2)
            print(f"The area for a triangel with the base {Base} and the height {Height} is {Area}")

        elif Shape2d == "Rectangle":
            Base = input("What is the base of the object ")
            Height = input("What is the height of the object ")
            Area = calculator(float(Base), "*", float(Height))
            print(f"The area for a rectangle with the base {Base} and the height {Height} is {Area}")

        elif Shape2d == "Parallellogram":
            Base = input("What is the base of the object ")
            Height = input("What is the height of the object ")
            Area = calculator(float(Base), "*", float(Height))
            print(f"The area for a parallellogram with the base {Base} and the height {Height} is {Area}")

        elif Shape2d == "Parallel_trapezoid":
            SideA = input("How long is the short side ")
            SideB = input("How long is the long side ")
            Height = input("What is the height ")
            Produkt1 = calculator(float(Height), "*", float(SideA))
            Produkt2 = calculator(float(Height), "*", float(SideB))
            Summa = calculator(Produkt1, "+", Produkt2)
            Area = calculator(Summa, "/", 2)
            print(f"A parallel trapezoid with the sides {SideA} and {SideB} has the area {Area}")

        elif Shape2d == "Circle":
            radius = float(input("What is the radius of the circle "))
            area = calculator(math.pi, "*", calculator(radius, "**", 2))
            Circumference = calculator(calculator(radius, "*", 2), "*", math.pi)
            print(f"The area of a cicle with radius {radius} is {area} and the circumference is {Circumference}")