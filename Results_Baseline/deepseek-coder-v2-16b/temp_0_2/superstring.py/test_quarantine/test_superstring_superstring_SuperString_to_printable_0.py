
# Module: superstring.superstring
import pytest
from superstring.superstring import add_numbers, SuperString, SuperStringSubstring, SuperStringUpper

# Test cases for add_numbers function
def test_add_numbers_integers():
    assert add_numbers(3, 4) == 7

def test_add_numbers_floats():
    assert add_numbers(3.5, 2.1) == 5.6

def test_add_numbers_invalid_type():
    with pytest.raises(TypeError):
        add_numbers("hello", 4)

# Test cases for SuperString class
def test_superstring_init():
    s = SuperString("Hello, World!")
    assert s._content == "Hello, World!"

def test_superstring_to_printable_default():
    s = SuperString("Hello, World!")
    assert s.to_printable() == "Hello, World!"

def test_superstring_to_printable_with_indices():
    s = SuperString("Hello, World!")
    assert s.to_printable(start_index=7) == "World!"
    assert s.to_printable(end_index=5) == "Hello"

def test_superstring_length():
    s = SuperString("Hello")
    assert s.length() == 5

# Test cases for SuperStringSubstring class
def test_superstringsubstring_init():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss._base == "Hello, World!" and sss._start == 7 and sss._end == 12

def test_superstringsubstring_get_substring():
    sss = SuperStringSubstring("Hello, World!", 7, 12)
    assert sss.get_substring() == "World!"

def test_superstringsubstring_length():
    sss = SuperStringSubstring("Hello", 0, 4)
    assert sss.length() == 5

# Test cases for SuperStringUpper class
def test_superstringupper_init():
    s = SuperStringUpper("hello world")
    assert s._base == "hello world"

def test_superstringupper_upper():
    s = SuperStringUpper("hello world")
    assert s.upper()._base == "HELLO WORLD"

def test_superstringupper_lower():
    s = SuperStringUpper("HELLO WORLD")
    assert s.lower()._base == "hello world"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperString_to_printable_0
superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_to_printable_0.py:4:0: E0611: No name 'add_numbers' in module 'superstring.superstring' (no-name-in-module)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_to_printable_0.py:38:44: E1101: Instance of 'SuperStringSubstring' has no '_start' member (no-member)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_to_printable_0.py:38:64: E1101: Instance of 'SuperStringSubstring' has no '_end' member (no-member)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_to_printable_0.py:42:11: E1101: Instance of 'SuperStringSubstring' has no 'get_substring' member (no-member)


"""