import pytest
from ultra_calculator.equation_solver import parse_equation, solve_equation, equation_solver, parse_token, parse_expression, linear_form, Node, Value, BinaryOp, Variable, Equation

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

# Test to_string

def test_node_to_string():
    with pytest.raises(NotImplementedError):
        Node().to_string()

def test_value_to_string():
    value = Value(5)

    assert value.to_string() == "5"

def test_variable_to_string():
    variable = Variable("x")

    assert variable.to_string() == "x"

def test_binary_op_to_string_parentheses():
    left = BinaryOp(
        BinaryOp(Value(2), "+", Value(3)),
        "*",
        Value(4)
    )

    right = BinaryOp(
        Value(2),
        "*",
        BinaryOp(Value(3), "+", Value(4))
    )

    assert left.to_string() == "(2 + 3) * 4"
    assert right.to_string() == "2 * (3 + 4)"

def test_binary_op_to_string_without_parentheses():
    expression = BinaryOp(
        BinaryOp(Value(2), "*", Value(3)),
        "+",
        Value(4)
    )

    assert expression.to_string() == "2 * 3 + 4"

# BinaryOp precedence test

def test_binary_op_precedence():
    assert BinaryOp(Value(1), "+", Value(2)).precedence() == 1
    assert BinaryOp(Value(1), "-", Value(2)).precedence() == 1
    assert BinaryOp(Value(1), "*", Value(2)).precedence() == 2
    assert BinaryOp(Value(1), "/", Value(2)).precedence() == 2
    assert BinaryOp(Value(1), "^", Value(2)).precedence() == 0

# Parse token tests

def test_parse_token_negative_variable():
    result = parse_token("-x")

    assert result.to_string() == "-1 * x"


def test_parse_token_number():
    result = parse_token("5")

    assert result.to_string() == "5.0"

def test_parse_token_variable():
    result = parse_token("x")

    assert result.to_string() == "x"

def test_parse_token_coefficient_variable():
    result = parse_token("2x")

    assert result.to_string() == "2.0 * x"

# Parse expression tests

def test_parse_expression_parentheses():
    result = parse_expression("(x + 5)")

    assert result.to_string() == "x + 5.0"

def test_parse_expression_binary_operation():
    result = parse_expression("2 + x")

    assert result.to_string() == "2.0 + x"

def test_parse_expression_multiplication():
    result = parse_expression("2 * x")

    assert result.to_string() == "2.0 * x"

def test_parse_expression_nested():
    result = parse_expression("2 * (x + 3)")

    assert result.to_string() == "2.0 * (x + 3.0)"

def test_parse_expression_parentheses_not_fully_enclosed():
    with pytest.raises(ValueError):
        parse_expression("(x + 5)(2)")

# Test for turning a equation into a string

def test_equation_to_string():
    equation = Equation(
        Variable("x"),
        Value(5)
    )

    assert equation.to_string() == "x = 5"

# Test for unsupported operator

def test_linear_form_unsupported_operator():
    expression = BinaryOp(Value(2), "^", Value(3))

    with pytest.raises(ValueError, match="Unsupported expression"):
        solve_equation(Equation(expression, Value(8)))

# Test equation solver divding by zero

def test_equation_solver_error(capsys):
    result = equation_solver("x / 0 = 2")

    captured = capsys.readouterr()

    assert result is None
    assert "Error: Division by zero" in captured.out

# Test multiplication on left side
def test_multiplication_with_variable_on_left():
    equation = parse_equation("x * 3 = 12")
    assert solve_equation(equation) == 4

# Test linear form

def test_linear_form_multiplication_of_constants():
    expression = BinaryOp(Value(2), "*", Value(3))
    assert linear_form(expression) == (0, 6)

def test_linear_form_division():
    expression = BinaryOp(
        Variable("x"),
        "/",
        Value(2)
    )

    assert linear_form(expression) == (0.5, 0)