import pytest
from ultra_calculator.calculator import calculator

# Simple tests for all of the operators

def test_addition():
    assert calculator(5, "+", 3) == 8

def test_subtraction():
    assert calculator(7, "-", 2) == 5

def test_multiplication():
    assert calculator(5, "*", 9) == 45

def test_division():
    assert calculator(45, "/", 5) == 9

def test_exponent():
    assert calculator(4, "**", 2) == 16

# Division with zero

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator(5, "/", 0)

def test_modulo_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator(5, "%", 0)

# Test with decimals and negative numbers

def test_negative_numbers():
    assert calculator(-5, "+", 3) == -2


def test_decimal_numbers():
    assert calculator(2.5, "*", 4) == 10

def test_invalid_operator():
    with pytest.raises(ValueError):
        calculator(5, "?", 3)