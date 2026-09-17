import pytest
from ultra_calculator.equation_solver import parse_equation, solve_equation, equation_solver

# Normal tests for some simple cases such as negative coefficient

def test_solve_simple_equation():
    equation = parse_equation("2x + 5 = 13")
    assert solve_equation(equation) == 4


def test_solve_equation_with_x_alone():
    equation = parse_equation("x + 4 = 9")
    assert solve_equation(equation) == 5


def test_solve_equation_with_negative_coefficient():
    equation = parse_equation("10 - 2x = 4")
    assert solve_equation(equation) == 3


def test_solve_equation_with_x_on_both_sides():
    equation = parse_equation("2x + 3 = x + 10")
    assert solve_equation(equation) == 7

# Test empty inputs

def test_empty_equation():
    with pytest.raises(ValueError):
        parse_equation("")


def test_whitespace_only_equation():
    with pytest.raises(ValueError):
        parse_equation("   ")

# Tests for wierd input

def test_equation_without_equals():
    with pytest.raises(ValueError):
        parse_equation("2x + 5")


def test_equation_with_multiple_equals():
    with pytest.raises(ValueError):
        parse_equation("2x + 5 = 13 = 20")


def test_equation_with_missing_left_side():
    with pytest.raises(ValueError):
        parse_equation("= 13")


def test_equation_with_missing_right_side():
    with pytest.raises(ValueError):
        parse_equation("2x + 5 =")

# Invalid expressions

def test_non_linear_expression():
    with pytest.raises(ValueError):
        solve_equation(parse_equation("x * x = 4"))


def test_division_by_x():
    with pytest.raises(ValueError):
        solve_equation(parse_equation("x / x = 2"))


def test_division_by_zero():
    with pytest.raises(ValueError):
        solve_equation(parse_equation("x / 0 = 2"))

# Test infinite and no solution scenarios

def test_infinitely_many_solutions():
    with pytest.raises(ValueError):
        solve_equation(parse_equation("2x + 4 = 2x + 4"))


def test_no_solution():
    with pytest.raises(ValueError):
        solve_equation(parse_equation("2x + 4 = 2x + 7"))

# More complex valid equations

def test_negative_x_coefficient():
    equation = parse_equation("-2x + 5 = 1")

    assert solve_equation(equation) == 2


def test_x_on_right_side():
    equation = parse_equation("10 = 2x + 4")

    assert solve_equation(equation) == 3


def test_parenthesized_equation():
    equation = parse_equation("(2x + 3) = 11")

    assert solve_equation(equation) == 4

# Test printing and asking

def test_equation_solver_print(capsys):
    result = equation_solver("2x + 4 = 10", shouldPrint=True)
    captured = capsys.readouterr()

    assert result == 3
    assert "x = 3" in captured.out

def test_equation_solver_ask(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2x + 4 = 10")

    result = equation_solver(None, shouldAsk=True)

    assert result == 3