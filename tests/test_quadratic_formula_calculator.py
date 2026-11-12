import pytest
from ultra_calculator.quadratic_formula_calculator import quadratic_formula_calculator
from cmath import sqrt

def test_quadratic_formula_two_solutions():
    x1, x2 = quadratic_formula_calculator(1, -5, 6)

    assert x1 == pytest.approx(3)
    assert x2 == pytest.approx(2)

def test_quadratic_formula_one_solution():
    x1, x2 = quadratic_formula_calculator(1, -2, 1)

    assert x1 == pytest.approx(1)
    assert x2 is None

def test_quadratic_formula_complex_solutions():
    x1, x2 = quadratic_formula_calculator(1, 0, 1)

    assert x1 == pytest.approx(1j)
    assert x2 == pytest.approx(-1j)

def test_quadratic_formula_print_two_solutions(capsys):
    quadratic_formula_calculator(1, -5, 6, True)

    captured = capsys.readouterr()

    assert captured.out == "x1 = 3.0\nx2 = 2.0\n"

def test_quadratic_formula_print_one_solution(capsys):
    quadratic_formula_calculator(1, -2, 1, True)

    captured = capsys.readouterr()

    assert captured.out == "x = 1.0\n"

def test_quadratic_formula_print_complex_solutions(capsys):
    quadratic_formula_calculator(1, 0, 1, True)

    captured = capsys.readouterr()

    assert captured.out == "x1 = 1.0i\nx2 = -1.0i\n"

def test_quadratic_formula_ask(monkeypatch):
    inputs = iter(["1", "-5", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    x1, x2 = quadratic_formula_calculator(None, None, None, shouldAsk=True)

    assert x1 == pytest.approx(3)
    assert x2 == pytest.approx(2)

def test_quadratic_formula_ask_complex(monkeypatch):
    inputs = iter(["1", "0", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    x1, x2 = quadratic_formula_calculator(None, None, None, shouldAsk=True)

    assert x1 == pytest.approx(1j)
    assert x2 == pytest.approx(-1j)

def test_quadratic_formula_a_zero(monkeypatch):
    inputs = iter(["0", "1", "-5", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    x1, x2 = quadratic_formula_calculator(None, None, None, shouldAsk=True)

    assert x1 == pytest.approx(3)
    assert x2 == pytest.approx(2)

@pytest.mark.parametrize(
    "a, b, c, expected1, expected2",
    [
        (1, 0, -4, 2, -2),
        (0.5, -2, 1.5, 3, 1),
        (-1, 0, 4, -2, 2),
    ]
)
def test_quadratic_formula_coefficient_variations(a, b, c, expected1, expected2):
    x1, x2 = quadratic_formula_calculator(a, b, c)

    assert x1 == pytest.approx(expected1)
    assert x2 == pytest.approx(expected2)

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 0, 1, "x1 = 1.0i\nx2 = -1.0i\n"),
        (1, 0, 4, "x1 = 2.0i\nx2 = -2.0i\n"),
    ]
)
def test_quadratic_formula_complex_printing(a, b, c, expected, capsys):
    quadratic_formula_calculator(a, b, c, True)

    captured = capsys.readouterr()
    assert captured.out == expected

@pytest.mark.parametrize(
    "inputs",
    [
        ["hello", "1", "-5", "6"],
        ["1", "hello", "-5", "6"],
        ["1", "-5", "hello", "6"],
        ["0", "1", "-5", "6"],
    ]
)
def test_quadratic_formula_invalid_input(monkeypatch, inputs):
    input_values = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_values))

    x1, x2 = quadratic_formula_calculator(None, None, None, shouldAsk=True)

    assert x1 == pytest.approx(3)
    assert x2 == pytest.approx(2)

def test_quadratic_formula_no_print(capsys):
    quadratic_formula_calculator(1, -5, 6)

    captured = capsys.readouterr()
    assert captured.out == ""

def test_quadratic_formula_mixed_complex_printing(capsys):
    quadratic_formula_calculator(1, -2, 2, True)

    captured = capsys.readouterr()

    assert captured.out == "x1 = 1.0 + 1.0i\nx2 = 1.0 - 1.0i\n"

def test_quadratic_formula_zero_constant():
    x1, x2 = quadratic_formula_calculator(1, -5, 0)

    assert x1 == pytest.approx(5)
    assert x2 == pytest.approx(0)

def test_quadratic_formula_imaginary_input(monkeypatch):
    inputs = iter(["1", "2i", "-3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    x1, x2 = quadratic_formula_calculator(None, None, None, shouldAsk=True)

    assert x1 == pytest.approx(sqrt(2) - 1j)
    assert x2 == pytest.approx(-sqrt(2) - 1j)