import pytest
from ultra_calculator.simplify_equations import simplify
from ultra_calculator.equation_solver import parse_expression

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