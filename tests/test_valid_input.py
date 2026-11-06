import pytest
from ultra_calculator.text_functions import get_valid_input


def test_get_valid_input_success(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")

    result = get_valid_input("Enter a number: ", float)

    assert result == 5.0


def test_get_valid_input_invalid_conversion(monkeypatch, capsys):
    inputs = iter(["abc", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_valid_input("Enter a number: ", float)

    captured = capsys.readouterr()

    assert result == 5.0
    assert captured.out.strip() == "Invalid input. Please try again."


def test_get_valid_input_invalid_validation(monkeypatch, capsys):
    inputs = iter(["2", "0.5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_valid_input(
        "Enter a number: ",
        float,
        lambda value: 0 <= value <= 1,
        "The value must be between 0 and 1."
    )

    captured = capsys.readouterr()

    assert result == 0.5
    assert captured.out.strip() == "The value must be between 0 and 1."