import pytest
from ultra_calculator.square_root_calculator import square_root

# Test different roots

def test_square_root():
    assert square_root(16, 2) == 4

def test_cube_root():
    assert square_root(27, 3) == 3

def test_fourth_root():
    assert square_root(81, 4) == 3

# Test decimal root

def test_square_root_decimal():
    assert square_root(2, 2) == 2 ** 0.5

def test_zero_root():
    with pytest.raises(ZeroDivisionError):
        square_root(16, 0)