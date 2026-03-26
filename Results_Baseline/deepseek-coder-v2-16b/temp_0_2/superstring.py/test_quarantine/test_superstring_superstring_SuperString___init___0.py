
# Module: superstring.superstring
# test_superstring.py
from superstring.superstring import add_numbers
import pytest

def test_add_numbers_integers():
    assert add_numbers(3, 4) == 7

def test_add_numbers_floats():
    assert add_numbers(3.5, 2.1) == 5.6

def test_add_numbers_invalid_type():
    with pytest.raises(TypeError):
        add_numbers("hello", 4)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperString___init___0
superstring.py/Test4DT_tests/test_superstring_superstring_SuperString___init___0.py:4:0: E0611: No name 'add_numbers' in module 'superstring.superstring' (no-name-in-module)


"""