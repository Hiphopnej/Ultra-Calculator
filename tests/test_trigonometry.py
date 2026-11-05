import pytest
import math
from ultra_calculator.trigonometry_calculator import trigonometry


@pytest.mark.parametrize(
    "function, value, unit, expected",
    [
        ("sin", 90, "degrees", 1.0),
        ("sin", math.pi / 2, "radians", 1.0),
        ("cos", 0, "degrees", 1.0),
        ("cos", 0, "radians", 1.0),
        ("tan", 45, "degrees", 1.0),
        ("tan", math.pi / 4, "radians", 1.0),
        ("arcsin", 1, "degrees", 90.0),
        ("arcsin", 1, "radians", round(math.pi / 2, 10)),
        ("arccos", 0, "degrees", 90.0),
        ("arccos", 0, "radians", round(math.pi / 2, 10)),
        ("arctan", 1, "degrees", 45.0),
        ("arctan", 1, "radians", round(math.pi / 4, 10)),
    ]
)

def test_trigonometry(function, value, unit, expected):
    result = trigonometry(function, value, unit)

    assert result == expected

@pytest.mark.parametrize(
    "function",
    ["invalid", "log", ""]
)
def test_invalid_trigonometric_function(function):
    with pytest.raises(ValueError, match="Invalid trigonometric function"):
        trigonometry(function, 1, "degrees", False, False)


@pytest.mark.parametrize(
    "unit",
    ["invalid", "meters", ""]
)
def test_invalid_angle_unit(unit):
    with pytest.raises(ValueError, match="Invalid angle unit"):
        trigonometry("sin", 1, unit, False, False)

@pytest.mark.parametrize(
    "function, value, unit, expected",
    [
        ("sin", 90, "degrees", "The sine of 90 in degrees is 1.0"),
        ("cos", 0, "radians", "The cosine of 0 in radians is 1.0"),
        ("tan", 45, "degrees", "The tangent of 45 in degrees is 1.0"),
        ("arcsin", 1, "degrees", "The arcsine of 1 in degrees is 90.0"),
        ("arccos", 0, "degrees", "The arccos of 0 in degrees is 90.0"),
        ("arctan", 1, "degrees", "The arctan of 1 in degrees is 45.0"),
    ]
)
def test_trigonometry_print(function, value, unit, expected, capsys):
    trigonometry(function, value, unit, True, False)

    captured = capsys.readouterr()
    assert captured.out.strip() == expected

def test_trigonometry_should_ask(monkeypatch):
    choices = iter(["Sin", "Degrees"])

    monkeypatch.setattr(
        "ultra_calculator.trigonometry_calculator.inquirer_input",
        lambda *args: next(choices)
    )

    monkeypatch.setattr(
        "ultra_calculator.trigonometry_calculator.get_valid_input",
        lambda *args: 90.0
    )

    result = trigonometry(None, None, None, False, True)

    assert result == 1.0

@pytest.mark.parametrize(
    "function, expected",
    [
        ("Arcsin", 90.0),
        ("Arccos", 0.0)
    ]
)
def test_trigonometry_inverse_input_validation(monkeypatch, function, expected):
    choices = iter([function, "Degrees"])

    monkeypatch.setattr(
        "ultra_calculator.trigonometry_calculator.inquirer_input",
        lambda *args: next(choices)
    )

    def mock_get_valid_input(message, conversion_func, validation_func=None, error_message=None):
        assert conversion_func is float
        assert validation_func(-1) is True
        assert validation_func(1) is True
        assert validation_func(2) is False
        return 1.0

    monkeypatch.setattr(
        "ultra_calculator.trigonometry_calculator.get_valid_input",
        mock_get_valid_input
    )

    result = trigonometry(None, None, None, False, True)

    assert result == expected