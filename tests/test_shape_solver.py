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