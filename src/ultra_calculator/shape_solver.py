import math
from ultra_calculator.calculator import calculator


def shape_solver(dimension, shape, shouldPrint=False, shouldAsk=False, **dimensions):
    if dimension != "2D":
        raise ValueError("Invalid dimension")

    shapes = [
        "Triangle",
        "Rectangle",
        "Parallellogram",
        "Parallel_trapezoid",
        "Circle"
    ]

    if shape not in shapes:
        raise ValueError("Invalid shape")

    if shouldAsk:
        if shape == "Triangle":
            dimensions["base"] = float(input("What is the base of the object "))
            dimensions["height"] = float(input("What is the height of the object "))
        elif shape == "Rectangle":
            dimensions["base"] = float(input("What is the base of the object "))
            dimensions["height"] = float(input("What is the height of the object "))
        elif shape == "Parallellogram":
            dimensions["base"] = float(input("What is the base of the object "))
            dimensions["height"] = float(input("What is the height of the object "))
        elif shape == "Parallel_trapezoid":
            dimensions["side_a"] = float(input("How long is the short side "))
            dimensions["side_b"] = float(input("How long is the long side "))
            dimensions["height"] = float(input("What is the height "))
        elif shape == "Circle":
            dimensions["radius"] = float(input("What is the radius of the circle "))

    if shape == "Triangle":
        base = dimensions["base"]
        height = dimensions["height"]
        area = calculator(base, "*", height)
        area = calculator(area, "/", 2)

        result = {"area": area}

        if shouldPrint:
            print(f"The area for a triangle with the base {base} and the height {height} is {area}")

        return result

    if shape == "Rectangle":
        base = dimensions["base"]
        height = dimensions["height"]
        area = calculator(base, "*", height)

        result = {"area": area}

        if shouldPrint:
            print(f"The area for a rectangle with the base {base} and the height {height} is {area}")

        return result

    if shape == "Parallellogram":
        base = dimensions["base"]
        height = dimensions["height"]
        area = calculator(base, "*", height)

        result = {"area": area}

        if shouldPrint:
            print(f"The area for a parallelogram with the base {base} and the height {height} is {area}")

        return result

    if shape == "Parallel_trapezoid":
        side_a = dimensions["side_a"]
        side_b = dimensions["side_b"]
        height = dimensions["height"]

        area = calculator(height, "*", side_a)
        area_2 = calculator(height, "*", side_b)
        area = calculator(area, "+", area_2)
        area = calculator(area, "/", 2)

        result = {"area": area}

        if shouldPrint:
            print(f"A parallel trapezoid with the sides {side_a} and {side_b} has the area {area}")

        return result

    if shape == "Circle":
        radius = dimensions["radius"]

        area = calculator(radius, "**", 2)
        area = calculator(math.pi, "*", area)

        circumference = calculator(radius, "*", 2)
        circumference = calculator(circumference, "*", math.pi)

        result = {
            "area": area,
            "circumference": circumference
        }

        if shouldPrint:
            print(f"The area of a circle with radius {radius} is {area} and the circumference is {circumference}")

        return result