import pytest

from ultra_calculator.equation_solver import parse_expression, Variable, Value, BinaryOp, Grouped, Equation
from ultra_calculator.derivative_solver import derivative_solver

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("5", "0"),
        ("x", "1"),
        ("x + 5", "1"),
        ("x - 5", "1"),
        ("x * x", "x + x"),
        ("x / x", "(x - x) / (x * x)"),
        ("5 * x", "5.0"),
        ("x / 5", "0.2"),
        ("x * (x + 5)", "x + 5.0 + x"),
        ("(x + 5) / (x - 2)", "(x - 2.0 - (x + 5.0)) / ((x - 2.0) * (x - 2.0))"),
        ("(x + 2)^2", "2.0 * (x + 2.0)"),
        ("2^x", "2.0 ^ x * ln(2.0)"),
        ("2^(x+3)", "2.0 ^ (x + 3.0) * ln(2.0)"),
        ("3^(2*x)", "3.0 ^ (2.0 * x) * ln(3.0) * 2.0"),
        ("2^(x^2)", "2.0 ^ x ^ 2.0 * ln(2.0) * (2.0 * x)"),
        ("2^(x*x)", "2.0 ^ (x * x) * ln(2.0) * (x + x)"),
        ("2^(x/2)", "2.0 ^ (x / 2.0) * ln(2.0) * 0.5"),
        ("ln(x)", "1 / x"),
        ("ln(x + 2)", "1 / (x + 2.0)"),
        ("ln(5)", "0.0"),
        ("ln(x * x)", "(x + x) / (x * x)"),
        ("log(x, 2)", "1 / (x * ln(2.0))"),
        ("log(x + 2, 5)", "1 / ((x + 2.0) * ln(5.0))"),
        ("log(x * x, 3)", "(x + x) / ((x * x) * ln(3.0))"),
        ("e^x", "e ^ x * ln(e)"),
        ("e^(3x)", "e ^ (3.0 * x) * ln(e) * 3.0"),
        ("e^(5x)", "e ^ (5.0 * x) * ln(e) * 5.0"),
        ("1 / x", "-1.0 / (x * x)"),
    ]
)
def test_derivative(expression, expected):
    node = parse_expression(expression)

    result = derivative_solver(node)

    assert result.to_string() == expected

@pytest.mark.parametrize(
    "expression",
    [
        "x * (x + 5)",
        "(x + 5) / (x - 2)",
    ]
)
def test_derivative_nested_expressions(expression):
    node = parse_expression(expression)

    result = derivative_solver(node)

    assert result is not None

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("x^2", "x ^ 2.0"),
        ("x^2^3", "x ^ 2.0 ^ 3.0"),
        ("(x^2)^3", "(x ^ 2.0) ^ 3.0"),
        ("x^(2+3)", "x ^ (2.0 + 3.0)"),
        ("x^2 * 3", "x ^ 2.0 * 3.0"),
        ("x + 2^3", "x + 2.0 ^ 3.0"),
    ]
)
def test_parse_exponentiation(expression, expected):
    assert parse_expression(expression).to_string() == expected

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("x - (x - 2)", "x - (x - 2.0)"),
        ("x / (x * 2)", "x / (x * 2.0)"),
        ("x / (x / 2)", "x / (x / 2.0)"),
        ("(x + 2) * 3", "(x + 2.0) * 3.0"),
        ("(x * 2) + 3", "x * 2.0 + 3.0"),
    ]
)
def test_binary_op_grouping(expression, expected):
    assert parse_expression(expression).to_string() == expected

def test_exponentiation_is_right_associative():
    result = parse_expression("x^2^3")

    assert result.operator == "^"
    assert isinstance(result.left, Variable)
    assert isinstance(result.right, BinaryOp)
    assert result.right.operator == "^"

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("sin(x)", "cos(x)"),
        ("sin(x + 2)", "cos(x + 2.0)"),
        ("sin(x * x)", "cos(x * x) * (x + x)"),
        ("sin(x ^ 2)", "cos(x ^ 2.0) * (2.0 * x)"),
        ("cos(x)", "-1 * sin(x)"),
        ("cos(x + 2)", "-1 * sin(x + 2.0)"),
        ("cos(x * x)", "-1 * sin(x * x) * (x + x)"),
        ("cos(x ^ 2)", "-1 * sin(x ^ 2.0) * (2.0 * x)"),
        ("tan(x)", "1 / cos(x) ^ 2"),
        ("tan(x + 2)", "1 / cos(x + 2.0) ^ 2"),
        ("tan(x * x)", "1 / cos(x * x) ^ 2 * (x + x)"),
        ("tan(x ^ 2)", "1 / cos(x ^ 2.0) ^ 2 * (2.0 * x)"),
    ]
)
def test_derivative_trigonometry(expression, expected):
    result = derivative_solver(parse_expression(expression))

    assert result.to_string() == expected

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("x", "1"),
        ("x ^ 2", "2.0 * x"),
        ("sin(x)", "cos(x)"),
        ("ln(x)", "1 / x"),
        ("tan(x)", "1 / cos(x) ^ 2"),
    ]
)
def test_derivative_string_input(expression, expected):
    result = derivative_solver(expression)

    assert result.to_string() == expected

def test_derivative_should_ask_invalid_input(monkeypatch):
    inputs = iter(["hello", "x ^ 2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = derivative_solver(shouldAsk=True)

    assert result.to_string() == "2.0 * x"

def test_derivative_should_ask_prints_error(monkeypatch, capsys):
    inputs = iter(["hello", "x"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    derivative_solver(shouldAsk=True)

    captured = capsys.readouterr()

    assert "Invalid mathematical expression" in captured.out

def test_derivative_should_print(capsys):
    result = derivative_solver("x ^ 2", shouldPrint=True)

    captured = capsys.readouterr()

    assert captured.out.strip() == "2.0 * x"
    assert result.to_string() == "2.0 * x"


def test_derivative_should_not_print(capsys):
    derivative_solver("x ^ 2")

    captured = capsys.readouterr()

    assert captured.out == ""

def test_derivative_invalid_string_without_asking():
    with pytest.raises(ValueError):
        derivative_solver("hello")

def test_derivative_grouped_expression():
    expression = Grouped(Variable("x"))

    result = derivative_solver(expression)

    assert result.to_string() == "(1)"

def test_derivative_unsupported_expression():
    expression = Equation(Variable("x"), Value(5))

    with pytest.raises(ValueError, match="Unsupported expression"):
        derivative_solver(expression)


def test_derivative_unsupported_operator():
    expression = BinaryOp(Variable("x"), "%", Value(2))

    with pytest.raises(ValueError, match="Unsupported operator"):
        derivative_solver(expression)