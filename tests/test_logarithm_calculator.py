import pytest
from math import e, log
from ultra_calculator.logarithm_calculator import logarithm_calculator


def test_natural_logarithm():
    result = logarithm_calculator(e, None, False, False)
    assert result == pytest.approx(1)

def test_logarithm_with_base():
    result = logarithm_calculator(8, 2, False, False)
    assert result == pytest.approx(3)

def test_natural_logarithm_print(capsys):
    logarithm_calculator(e, None, True, False)

    captured = capsys.readouterr()
    assert captured.out == "The logarithm of 2.718281828459045 with base e is 1.0\n"

def test_logarithm_with_base_print(capsys):
    logarithm_calculator(8, 2, True, False)

    captured = capsys.readouterr()
    assert captured.out == "The logarithm of 8 with base 2 is 3.0\n"

def test_logarithm_ask_natural(monkeypatch):
    inputs = iter(["2.718281828459045", "e"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = logarithm_calculator(None, None, False, True)

    assert result == pytest.approx(1)

def test_logarithm_ask_with_base(monkeypatch):
    inputs = iter(["8", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = logarithm_calculator(None, None, False, True)

    assert result == pytest.approx(3)

def test_logarithm_ask_invalid_number(monkeypatch):
    inputs = iter(["hello", "0", "-5", "8", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = logarithm_calculator(None, None, False, True)

    assert result == pytest.approx(3)

def test_logarithm_ask_invalid_base(monkeypatch):
    inputs = iter(["8", "hello", "0", "1", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = logarithm_calculator(None, None, False, True)

    assert result == pytest.approx(3)

def test_logarithm_ask_uppercase_e(monkeypatch):
    inputs = iter(["2.718281828459045", "E"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = logarithm_calculator(None, None, False, True)

    assert result == pytest.approx(1)

def test_logarithm_float_base():
    result = logarithm_calculator(8, 2.5, False, False)
    assert result == pytest.approx(log(8, 2.5))

@pytest.mark.parametrize("value", [0, -1, -10])
def test_logarithm_invalid_value(value):
    with pytest.raises(ValueError):
        logarithm_calculator(value, None, False, False)

@pytest.mark.parametrize("value", ["hello", None, True, False])
def test_logarithm_invalid_value_type(value):
    with pytest.raises(TypeError):
        logarithm_calculator(value, None, False, False)

@pytest.mark.parametrize("value", [0, -1, -10, float("nan"), float("inf"), float("-inf")])
def test_logarithm_invalid_value(value):
    with pytest.raises(ValueError):
        logarithm_calculator(value, None, False, False)

@pytest.mark.parametrize("base", ["hello", True, False, []])
def test_logarithm_invalid_base_type(base):
    with pytest.raises(TypeError):
        logarithm_calculator(8, base, False, False)

@pytest.mark.parametrize("base", [1, 0, -1, 0.5, float("nan"), float("inf"), float("-inf")])
def test_logarithm_invalid_base(base):
    with pytest.raises(ValueError):
        logarithm_calculator(8, base, False, False)

def test_logarithm_ask_invalid_number(monkeypatch):
    inputs = iter([
        "hello",
        "0",
        "-5",
        "nan",
        "inf",
        "8",
        "2"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = logarithm_calculator(None, None, False, True)

    assert result == pytest.approx(3)

def test_logarithm_ask_invalid_base(monkeypatch):
    inputs = iter([
        "8",
        "hello",
        "0",
        "1",
        "-2",
        "0.5",
        "nan",
        "inf",
        "2"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = logarithm_calculator(None, None, False, True)

    assert result == pytest.approx(3)

def test_logarithm_ask_uppercase_e(monkeypatch):
    inputs = iter(["2.718281828459045", "E"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = logarithm_calculator(None, None, False, True)

    assert result == pytest.approx(1)

def test_logarithm_ask_float_base(monkeypatch):
    inputs = iter(["8", "2.5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = logarithm_calculator(None, None, False, True)

    assert result == pytest.approx(log(8, 2.5))