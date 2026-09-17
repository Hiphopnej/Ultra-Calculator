from ultra_calculator.konjugatregeln import fix_num, konjugatregeln

def test_konjugatregeln_basic():
    assert fix_num("x", "3") == "x^2-9"

def test_konjugatregeln_coefficients():
    assert fix_num("2x", "3") == "4x^2-9"

def test_konjugatregeln_two_variables():
    assert fix_num("2x", "3x") == "-5x^2"

def test_konjugatregeln_constants():
    assert fix_num("5", "3") == "16"

def test_konjugatregeln_negative_term():
    assert fix_num("x", "-3") == "x^2-9"

def test_konjugatregeln():
    assert konjugatregeln("x", "3") == "x^2-9"

def test_konjugatregeln_print(capsys):
    konjugatregeln("x", "3", shouldPrint=True)
    captured = capsys.readouterr()
    assert captured.out == "x^2-9\n"

def test_konjugatregeln_ask(monkeypatch):
    inputs = iter(["x", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert konjugatregeln(None, None, shouldAsk=True) == "x^2-9"