from ultra_calculator.pq_solver import pq_solver

# Test real solution
def test_pq_solver_two_real_solutions():
    x1, x2 = pq_solver(-5, 6)
    assert x1 == 3
    assert x2 == 2

# Test double root
def test_pq_solver_one_repeated_solution():
    x1, x2 = pq_solver(-4, 4)
    assert x1 == 2
    assert x2 == 2

# Test complex solution
def test_pq_solver_complex_solutions():
    x1, x2 = pq_solver(0, 4)
    assert x1 == 2j
    assert x2 == -2j

# Test printing
def test_pq_solver_print(capsys):
    pq_solver(-5, 6, shouldPrint=True)

    captured = capsys.readouterr()

    assert "x1 = 3.0" in captured.out
    assert "x2 = 2.0" in captured.out

def test_pq_solver_ask(monkeypatch):
    inputs = iter(["-5", "6"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    x1, x2 = pq_solver(0, 0, shouldAsk=True)

    assert x1 == 3
    assert x2 == 2