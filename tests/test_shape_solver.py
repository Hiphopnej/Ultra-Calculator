import math
import pytest
from ultra_calculator.shape_solver import shape_solver

# Test different 2D shapes

def test_triangle():
    result = shape_solver("2D", "Triangle", base=3, height=4)
    assert result["area"] == 6

def test_rectangle():
    result = shape_solver("2D", "Rectangle", base=3, height=4)
    assert result["area"] == 12

def test_parallelogram():
    result = shape_solver("2D", "Parallellogram", base=3, height=4)
    assert result["area"] == 12

def test_parallel_trapezoid():
    result = shape_solver("2D", "Parallel_trapezoid", side_a=3, side_b=5, height=4)
    assert result["area"] == 16

def test_circle():
    result = shape_solver("2D", "Circle", radius=5)
    assert math.isclose(result["area"], math.pi * 25)
    assert math.isclose(result["circumference"], math.pi * 10)

# Test invalid scenarios

def test_invalid_dimension():
    with pytest.raises(ValueError):
        shape_solver("4D", "Circle", radius=5)

def test_invalid_shape():
    with pytest.raises(ValueError):
        shape_solver("2D", "Square", side=5)

def test_shape_solver_print(capsys):
    result = shape_solver("2D", "Triangle", base=3, height=4, shouldPrint=True)

    captured = capsys.readouterr()

    assert result["area"] == 6
    assert "The area for a triangle" in captured.out
    assert "6" in captured.out

def test_shape_solver_ask(monkeypatch):
    inputs = iter(["3", "4"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = shape_solver("2D", "Triangle", shouldAsk=True)

    assert result["area"] == 6

# Test 3D shapes

def test_cuboid():
    result = shape_solver("3D", "Cuboid", base_surface=10, height=5)
    assert result["volume"] == 50


def test_prism():
    result = shape_solver("3D", "Prism", base_surface=10, height=5)
    assert result["volume"] == 50


def test_cylinder():
    result = shape_solver("3D", "Cylinder", radius=5, height=10)
    assert math.isclose(result["volume"], math.pi * 25 * 10)
    assert math.isclose(result["mantle_area"], 2 * math.pi * 5 * 10)


def test_pyramid():
    result = shape_solver("3D", "Pyramid", base_surface=10, height=6)
    assert result["volume"] == 20


def test_cone():
    result = shape_solver("3D", "Cone", radius=3, height=4)
    assert math.isclose(result["volume"], 12 * math.pi)
    assert math.isclose(result["mantle_area"], 15 * math.pi)


def test_sphere():
    result = shape_solver("3D", "Sphere", radius=3)
    assert math.isclose(result["volume"], 36 * math.pi)
    assert math.isclose(result["area"], 36 * math.pi)

# Add the printing/asking tests for 3D

def test_shape_solver_3d_print(capsys):
    result = shape_solver("3D", "Cylinder", radius=5, height=10, shouldPrint=True)

    captured = capsys.readouterr()

    assert math.isclose(result["volume"], math.pi * 25 * 10)
    assert "The mantle area of the cylinder" in captured.out

def test_shape_solver_3d_ask(monkeypatch):
    inputs = iter(["10", "5"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = shape_solver("3D", "Cuboid", shouldAsk=True)

    assert result["volume"] == 50

# Test without dimensions

def test_shape_solver_missing_dimension():
    with pytest.raises(ValueError):
        shape_solver("2D", "Circle")


def test_shape_solver_missing_multiple_dimensions():
    with pytest.raises(ValueError):
        shape_solver("3D", "Cylinder", radius=5)

# More printing/asking tests

def test_shape_solver_triangle_print(capsys):
    result = shape_solver(
        "2D",
        "Triangle",
        shouldPrint=True,
        base=4,
        height=6
    )

    captured = capsys.readouterr()

    assert result == {"area": 12}
    assert "The area for a triangle with the base 4 and the height 6 is 12" in captured.out

def test_shape_solver_triangle_ask(monkeypatch):
    inputs = iter(["4", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = shape_solver("2D", "Triangle", shouldAsk=True)

    assert result == {"area": 12}

def test_shape_solver_rectangle_print(capsys):
    result = shape_solver(
        "2D",
        "Rectangle",
        shouldPrint=True,
        base=4,
        height=6
    )

    captured = capsys.readouterr()

    assert result == {"area": 24}
    assert "The area for a rectangle with the base 4 and the height 6 is 24" in captured.out

def test_shape_solver_rectangle_ask(monkeypatch):
    inputs = iter(["4", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = shape_solver("2D", "Rectangle", shouldAsk=True)

    assert result == {"area": 24}

def test_shape_solver_parallellogram_print(capsys):
    result = shape_solver(
        "2D",
        "Parallellogram",
        shouldPrint=True,
        base=4,
        height=6
    )

    captured = capsys.readouterr()

    assert result == {"area": 24}
    assert "The area for a parallelogram with the base 4 and the height 6 is 24" in captured.out

def test_shape_solver_parallellogram_ask(monkeypatch):
    inputs = iter(["4", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = shape_solver("2D", "Parallellogram", shouldAsk=True)

    assert result == {"area": 24}

def test_shape_solver_parallel_trapezoid_print(capsys):
    result = shape_solver(
        "2D",
        "Parallel_trapezoid",
        shouldPrint=True,
        side_a=4,
        side_b=8,
        height=6
    )

    captured = capsys.readouterr()

    assert result == {"area": 36}
    assert "A parallel trapezoid with the sides 4 and 8 has the area 36" in captured.out

def test_shape_solver_parallel_trapezoid_ask(monkeypatch):
    inputs = iter(["4", "8", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = shape_solver("2D", "Parallel_trapezoid", shouldAsk=True)

    assert result == {"area": 36}

def test_shape_solver_circle_print(capsys):
    result = shape_solver(
        "2D",
        "Circle",
        shouldPrint=True,
        radius=2
    )

    captured = capsys.readouterr()

    assert result["area"] == 4 * math.pi
    assert result["circumference"] == 4 * math.pi
    assert "The area of a circle with radius 2" in captured.out

def test_shape_solver_circle_ask(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")

    result = shape_solver("2D", "Circle", shouldAsk=True)

    assert result["area"] == 4 * math.pi
    assert result["circumference"] == 4 * math.pi

def test_shape_solver_cuboid_print(capsys):
    result = shape_solver(
        "3D",
        "Cuboid",
        shouldPrint=True,
        base_surface=4,
        height=6
    )

    captured = capsys.readouterr()

    assert result == {"volume": 24}
    assert "For a Cuboid with the base surface of 4 and height of 6 the volume is 24" in captured.out

def test_shape_solver_cuboid_ask(monkeypatch):
    inputs = iter(["4", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = shape_solver("3D", "Cuboid", shouldAsk=True)

    assert result == {"volume": 24}

def test_shape_solver_prism_print(capsys):
    result = shape_solver(
        "3D",
        "Prism",
        shouldPrint=True,
        base_surface=4,
        height=6
    )

    captured = capsys.readouterr()

    assert result == {"volume": 24}
    assert "For a Prism with the base surface of 4 and height of 6 the volume is 24" in captured.out

def test_shape_solver_prism_ask(monkeypatch):
    inputs = iter(["4", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = shape_solver("3D", "Prism", shouldAsk=True)

    assert result == {"volume": 24}

def test_shape_solver_cylinder_print(capsys):
    result = shape_solver(
        "3D",
        "Cylinder",
        shouldPrint=True,
        radius=2,
        height=6
    )

    captured = capsys.readouterr()

    assert result["volume"] == 24 * math.pi
    assert result["mantle_area"] == 24 * math.pi
    assert "For a Cylinder with radius 2 and height 6" in captured.out
    assert "The mantle area of the cylinder is" in captured.out

def test_shape_solver_cylinder_ask(monkeypatch):
    inputs = iter(["2", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = shape_solver("3D", "Cylinder", shouldAsk=True)

    assert result["volume"] == 24 * math.pi
    assert result["mantle_area"] == 24 * math.pi

def test_shape_solver_pyramid_print(capsys):
    result = shape_solver(
        "3D",
        "Pyramid",
        shouldPrint=True,
        base_surface=4,
        height=6
    )

    captured = capsys.readouterr()

    assert result == {"volume": 8}
    assert "For a Pyramid with the base surface of 4 and height of 6 the volume is 8" in captured.out

def test_shape_solver_pyramid_ask(monkeypatch):
    inputs = iter(["4", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = shape_solver("3D", "Pyramid", shouldAsk=True)

    assert result == {"volume": 8}

def test_shape_solver_cone_print(capsys):
    result = shape_solver(
        "3D",
        "Cone",
        shouldPrint=True,
        radius=3,
        height=4
    )

    captured = capsys.readouterr()

    assert result["volume"] == 12 * math.pi
    assert result["mantle_area"] == 15 * math.pi
    assert "For a Cone with radius 3 and height 4" in captured.out
    assert "The mantle area is" in captured.out

def test_shape_solver_cone_ask(monkeypatch):
    inputs = iter(["3", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = shape_solver("3D", "Cone", shouldAsk=True)

    assert result["volume"] == 12 * math.pi
    assert result["mantle_area"] == 15 * math.pi

def test_shape_solver_sphere_print(capsys):
    result = shape_solver(
        "3D",
        "Sphere",
        shouldPrint=True,
        radius=3
    )

    captured = capsys.readouterr()

    assert result["volume"] == 36 * math.pi
    assert result["area"] == 36 * math.pi
    assert "If the radius of the sphere is 3" in captured.out
    assert "The area of the sphere is" in captured.out

def test_shape_solver_sphere_ask(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")

    result = shape_solver("3D", "Sphere", shouldAsk=True)

    assert result["volume"] == 36 * math.pi
    assert result["area"] == 36 * math.pi

# Test invalid shape

def test_shape_solver_invalid_2d_shape():
    with pytest.raises(ValueError, match="Invalid shape"):
        shape_solver("2D", "Invalid")

def test_shape_solver_invalid_3d_shape():
    with pytest.raises(ValueError, match="Invalid shape"):
        shape_solver("3D", "Invalid")