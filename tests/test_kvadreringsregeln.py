import pytest
from ultra_calculator.kvadreringsregeln import add_term, parse_term, format_polynomial, fix_num, kvadreringsregeln

# Test parse term

def test_parse_term_constant():
    assert parse_term("5") == (5, 0)

def test_parse_term_x():
    assert parse_term("x") == (1, 1)

def test_parse_term_negative_x():
    assert parse_term("-x") == (-1, 1)

def test_parse_term_coefficient():
    assert parse_term("3x") == (3, 1)

def test_parse_term_power():
    assert parse_term("2x^3") == (2, 3)

def test_parse_term_spaces():
    assert parse_term(" 2 x ") == (2, 1)

def test_parse_term_double_star():
    assert parse_term("2x**3") == (2, 3)

# Test add term

def test_add_term_new_exponent():
    terms = {}
    add_term(terms, 3, 2)
    assert terms == {2: 3}

def test_add_term_existing_exponent():
    terms = {2: 3}
    add_term(terms, 5, 2)
    assert terms == {2: 8}

# Test format polynomial

def test_format_polynomial():
    assert format_polynomial({2: 3, 1: 2, 0: 5}) == "3x^2+2x+5"

def test_format_polynomial_negative():
    assert format_polynomial({2: 3, 1: -2, 0: -5}) == "3x^2-2x-5"

def test_format_polynomial_implicit_one():
    assert format_polynomial({2: 1, 1: 1}) == "x^2+x"

def test_format_polynomial_zero_terms():
    assert format_polynomial({2: 3, 1: 0, 0: 5}) == "3x^2+5"

def test_format_polynomial_all_zero():
    assert format_polynomial({2: 0, 1: 0, 0: 0}) == "0"

# Test fix num

def test_fix_num_addition():
    assert fix_num("x", "3", "+") == "x^2+6x+9"

def test_fix_num_subtraction():
    assert fix_num("x", "3", "-") == "x^2-6x+9"

def test_fix_num_two_variables():
    assert fix_num("2x", "3x", "+") == "25x^2"

def test_fix_num_negative_term():
    assert fix_num("-x", "3", "+") == "x^2-6x+9"

def test_fix_num_constants():
    assert fix_num("2", "3", "+") == "25"

def test_fix_num_powers():
    assert fix_num("2x^2", "3x", "+") == "4x^4+12x^3+9x^2"

# Test kvadreringsregeln

def test_kvadreringsregeln_addition():
    assert kvadreringsregeln("x", "3", "+") == "x^2+6x+9"

def test_kvadreringsregeln_subtraction():
    assert kvadreringsregeln("x", "3", "-") == "x^2-6x+9"

def test_kvadreringsregeln_print(capsys):
    kvadreringsregeln("x", "3", "+", shouldPrint=True)
    captured = capsys.readouterr()
    assert captured.out == "x^2+6x+9\n"

def test_kvadreringsregeln_ask(monkeypatch):
    inputs = iter(["x", "3", "+"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert kvadreringsregeln(None, None, None, shouldAsk=True) == "x^2+6x+9"

def test_kvadreringsregeln_invalid_operator():
    with pytest.raises(ValueError):
        kvadreringsregeln("x", "3", "*")