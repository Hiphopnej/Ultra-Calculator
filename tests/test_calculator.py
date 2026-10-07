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

def test_modulo():
    assert calculator(8,"%",2) == 0

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

def test_addition_print(capsys):
    result = calculator(5, "+", 3, shouldPrint=True)

    captured = capsys.readouterr()

    assert result == 8
    assert captured.out == "8\n"

def test_subtraction_print(capsys):
    result = calculator(7, "-", 2, shouldPrint=True)

    captured = capsys.readouterr()

    assert result == 5
    assert captured.out == "5\n"

def test_multiplication_print(capsys):
    result = calculator(5, "*", 9, shouldPrint=True)

    captured = capsys.readouterr()

    assert result == 45
    assert captured.out == "45\n"

def test_division_print(capsys):
    result = calculator(45, "/", 5, shouldPrint=True)

    captured = capsys.readouterr()

    assert result == 9.0
    assert captured.out == "9.0\n"

def test_exponent_print(capsys):
    result = calculator(4, "**", 2, shouldPrint=True)

    captured = capsys.readouterr()

    assert result == 16
    assert captured.out == "16\n"

def test_modulo_print(capsys):
    result = calculator(8, "%", 2, shouldPrint=True)

    captured = capsys.readouterr()

    assert result == 0
    assert captured.out == "0\n"

def test_calculator_ask(monkeypatch):
    inputs = iter(["7", "+", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = calculator(None, None, None, shouldAsk=True)

    assert result == 12