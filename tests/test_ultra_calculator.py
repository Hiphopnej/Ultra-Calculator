import pytest
import sys
import subprocess
from ultra_calculator.ultra_calculator import inquirer_input, main
import ultra_calculator.ultra_calculator as ultra_calculator

def test_inquirer_input(monkeypatch):
    class FakeSelect:
        def execute(self):
            return "calculator"

    monkeypatch.setattr("ultra_calculator.ultra_calculator.inquirer.select", lambda **kwargs: FakeSelect())

    result = inquirer_input("What do you want to calculate", ["calculator"])

    assert result == "calculator"

def test_main_calculator(monkeypatch):
    monkeypatch.setattr("ultra_calculator.ultra_calculator.inquirer_input", lambda message, options: "calculator")

    called = []

    monkeypatch.setattr("ultra_calculator.ultra_calculator.calculator", lambda *args: called.append(args))

    main()

    assert called == [(None, None, None, True, True)]


@pytest.mark.parametrize(
    "choice,function_name,expected_args",
    [
        ("square root", "square_root", (None, None, True, True)),
        ("pq solver", "pq_solver", (None, None, True, True)),
        ("pytagoras solver", "pytagoras_solver", (None, None, None, True, True)),
        ("shape solver", "shape_solver", (None, None, True, True)),
        ("kvadreringsregeln", "kvadreringsregeln", (None, None, None, True, True)),
        ("konjugatregeln", "konjugatregeln", (None, None, True, True)),
        ("equation solver", "equation_solver", (None, True, True)),
    ],
)

def test_main_choices(monkeypatch, choice, function_name, expected_args):
    monkeypatch.setattr(ultra_calculator, "inquirer_input", lambda message, options: choice,)

    called = []

    monkeypatch.setattr(ultra_calculator, function_name, lambda *args: called.append(args),)

    ultra_calculator.main()

    assert called == [expected_args]

def test_import_does_not_run_main():
    result = subprocess.run([sys.executable, "-c", "import ultra_calculator.ultra_calculator"], capture_output=True, text=True)

    assert result.returncode == 0