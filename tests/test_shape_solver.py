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