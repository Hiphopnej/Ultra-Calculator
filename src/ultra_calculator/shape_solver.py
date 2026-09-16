import math


def get_dimensions(dimensions, *required):
    for name in required:
        if name not in dimensions:
            raise ValueError(f"Missing dimension: {name}")


def shape_solver(dimension, shape, shouldPrint=False, shouldAsk=False, **dimensions):
    if dimension == "2D":
        if shape == "Triangle":
            if shouldAsk:
                dimensions["base"] = float(input("What is the base of the object "))
                dimensions["height"] = float(input("What is the height of the object "))

            get_dimensions(dimensions, "base", "height")

            base = dimensions["base"]
            height = dimensions["height"]
            area = base * height / 2

            result = {"area": area}

            if shouldPrint:
                print(f"The area for a triangle with the base {base} and the height {height} is {area}")

            return result

        if shape == "Rectangle":
            if shouldAsk:
                dimensions["base"] = float(input("What is the base of the object "))
                dimensions["height"] = float(input("What is the height of the object "))

            get_dimensions(dimensions, "base", "height")

            base = dimensions["base"]
            height = dimensions["height"]
            area = base * height

            result = {"area": area}

            if shouldPrint:
                print(f"The area for a rectangle with the base {base} and the height {height} is {area}")

            return result

        if shape == "Parallellogram":
            if shouldAsk:
                dimensions["base"] = float(input("What is the base of the object "))
                dimensions["height"] = float(input("What is the height of the object "))

            get_dimensions(dimensions, "base", "height")

            base = dimensions["base"]
            height = dimensions["height"]
            area = base * height

            result = {"area": area}

            if shouldPrint:
                print(f"The area for a parallelogram with the base {base} and the height {height} is {area}")

            return result

        if shape == "Parallel_trapezoid":
            if shouldAsk:
                dimensions["side_a"] = float(input("How long is the short side "))
                dimensions["side_b"] = float(input("How long is the long side "))
                dimensions["height"] = float(input("What is the height "))

            get_dimensions(dimensions, "side_a", "side_b", "height")

            side_a = dimensions["side_a"]
            side_b = dimensions["side_b"]
            height = dimensions["height"]
            area = (side_a + side_b) * height / 2

            result = {"area": area}

            if shouldPrint:
                print(f"A parallel trapezoid with the sides {side_a} and {side_b} has the area {area}")

            return result

        if shape == "Circle":
            if shouldAsk:
                dimensions["radius"] = float(input("What is the radius of the circle "))

            get_dimensions(dimensions, "radius")

            radius = dimensions["radius"]
            area = math.pi * radius ** 2
            circumference = 2 * math.pi * radius

            result = {
                "area": area,
                "circumference": circumference
            }

            if shouldPrint:
                print(f"The area of a circle with radius {radius} is {area} and the circumference is {circumference}")

            return result

        raise ValueError("Invalid shape")

    if dimension == "3D":
        if shape == "Cuboid":
            if shouldAsk:
                dimensions["base_surface"] = float(input("What is the base surface of the object "))
                dimensions["height"] = float(input("What is the height of the object "))

            get_dimensions(dimensions, "base_surface", "height")

            base_surface = dimensions["base_surface"]
            height = dimensions["height"]
            volume = base_surface * height

            result = {"volume": volume}

            if shouldPrint:
                print(f"For a {shape} with the base surface of {base_surface} and height of {height} the volume is {volume}")

            return result

        if shape == "Prism":
            if shouldAsk:
                dimensions["base_surface"] = float(input("What is the base surface of the object "))
                dimensions["height"] = float(input("What is the height of the object "))

            get_dimensions(dimensions, "base_surface", "height")

            base_surface = dimensions["base_surface"]
            height = dimensions["height"]
            volume = base_surface * height

            result = {"volume": volume}

            if shouldPrint:
                print(f"For a {shape} with the base surface of {base_surface} and height of {height} the volume is {volume}")

            return result

        if shape == "Cylinder":
            if shouldAsk:
                dimensions["radius"] = float(input("What is the radius of the base surface "))
                dimensions["height"] = float(input("What is the height of the object "))

            get_dimensions(dimensions, "radius", "height")

            radius = dimensions["radius"]
            height = dimensions["height"]
            volume = math.pi * radius ** 2 * height
            mantle_area = 2 * math.pi * radius * height

            result = {
                "volume": volume,
                "mantle_area": mantle_area
            }

            if shouldPrint:
                print(f"For a {shape} with radius {radius} and height {height} the volume is {volume}")
                print(f"The mantle area of the cylinder is {mantle_area}")

            return result

        if shape == "Pyramid":
            if shouldAsk:
                dimensions["base_surface"] = float(input("What is the base surface of the object "))
                dimensions["height"] = float(input("What is the height of the object "))

            get_dimensions(dimensions, "base_surface", "height")

            base_surface = dimensions["base_surface"]
            height = dimensions["height"]
            volume = base_surface * height / 3

            result = {"volume": volume}

            if shouldPrint:
                print(f"For a {shape} with the base surface of {base_surface} and height of {height} the volume is {volume}")

            return result

        if shape == "Cone":
            if shouldAsk:
                dimensions["radius"] = float(input("What is the radius of the base surface "))
                dimensions["height"] = float(input("What is the height of the object "))

            get_dimensions(dimensions, "radius", "height")

            radius = dimensions["radius"]
            height = dimensions["height"]
            volume = math.pi * radius ** 2 * height / 3
            slope = math.sqrt(radius ** 2 + height ** 2)
            mantle_area = math.pi * radius * slope

            result = {
                "volume": volume,
                "mantle_area": mantle_area
            }

            if shouldPrint:
                print(f"For a {shape} with radius {radius} and height {height} the volume is {volume}")
                print(f"The mantle area is {mantle_area}")

            return result

        if shape == "Sphere":
            if shouldAsk:
                dimensions["radius"] = float(input("What is the radius of the object "))

            get_dimensions(dimensions, "radius")

            radius = dimensions["radius"]
            volume = 4 * math.pi * radius ** 3 / 3
            area = 4 * math.pi * radius ** 2

            result = {
                "volume": volume,
                "area": area
            }

            if shouldPrint:
                print(f"If the radius of the sphere is {radius} then the volume is {volume}")
                print(f"The area of the sphere is {area}")

            return result

        raise ValueError("Invalid shape")

    raise ValueError("Invalid dimension")