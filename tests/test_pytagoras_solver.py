import pytest
from ultra_calculator.pytagoras_solver import pytagoras_solver

# Test pytagoras on all of the sides

def test_pytagoras_solver_c():
    assert pytagoras_solver("c", a=3, b=4) == 5

def test_pytagoras_solver_a():
    assert pytagoras_solver("a", b=4, c=5) == 3

def test_pytagoras_solver_b():
    assert pytagoras_solver("b", a=3, c=5) == 4

# Test invalid side

def test_pytagoras_solver_invalid_side():
    with pytest.raises(ValueError):
        pytagoras_solver("d", a=3, b=4)

# Test printing

def test_side_a_print(capsys):
    pytagoras_solver("a", b=4, c=5, shouldPrint=True)
    captured = capsys.readouterr()

    assert "a is 3" in captured.out

def test_side_a_ask(monkeypatch):
    inputs = iter(["a", "4", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = pytagoras_solver(None, shouldAsk=True)

    assert result == 3

def test_side_b_print(capsys):
    pytagoras_solver("b", a=4, c=5, shouldPrint=True)
    captured = capsys.readouterr()

    assert "b is 3" in captured.out

def test_side_b_ask(monkeypatch):
    inputs = iter(["b", "4", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = pytagoras_solver(None, shouldAsk=True)

    assert result == 3

def test_side_c_print(capsys):
    pytagoras_solver("c", a=3, b=4, shouldPrint=True)
    captured = capsys.readouterr()

    assert "c is 5" in captured.out

def test_side_c_ask(monkeypatch):
    inputs = iter(["c", "3", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = pytagoras_solver(None, shouldAsk=True)

    assert result == 5