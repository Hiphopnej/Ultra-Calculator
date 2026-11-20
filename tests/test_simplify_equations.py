import pytest
from ultra_calculator.simplify_equations import simplify
from ultra_calculator.equation_solver import parse_expression, Value, BinaryOp, Variable

@pytest.mark.parametrize(
    "expression, expected",
    [
        ("0 + x", "x"),
        ("x + 0", "x"),
        ("x - 0", "x"),
        ("0 * x", "0"),
        ("x * 0", "0"),
        ("1 * x", "x"),
        ("x * 1", "x"),
        ("x / 1", "x"),
        ("2 + 3", "5.0"),
        ("2 * 3", "6.0"),
        ("x ^ 1", "x"),
        ("x ^ 0", "1"),
    ]
)
def test_simplify(expression, expected):
    result = simplify(parse_expression(expression))
    assert result.to_string() == expected

def test_simplify_power():
    result = simplify(BinaryOp(Value(2), "^", Value(3)))

    assert result.to_string() == "8"


def test_simplify_complex_power():
    result = simplify(BinaryOp(Value(-2), "^", Value(0.5)))

    assert isinstance(result, BinaryOp)


def test_simplify_power_overflow():
    result = simplify(BinaryOp(Value(10.0), "^", Value(10000.0)))

    assert isinstance(result, BinaryOp)

@pytest.mark.parametrize(
    "expression",
    [
        BinaryOp(Value(0), "*", Variable("x")),
        BinaryOp(Variable("x"), "*", Value(0)),
    ],
)
def test_simplify_multiplication_by_zero(expression):
    result = simplify(expression)

    assert result.to_string() == "0"

def test_simplify_zero_division():
    expression = BinaryOp(Value(0), "/", Variable("x"))

    result = simplify(expression)

    assert isinstance(result, Value)
    assert result.to_string() == "0"