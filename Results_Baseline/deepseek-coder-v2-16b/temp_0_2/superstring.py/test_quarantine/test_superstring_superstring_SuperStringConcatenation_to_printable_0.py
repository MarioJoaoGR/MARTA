
# Module: superstring.superstring
import pytest
from superstring.superstring import SuperStringConcatenation

# Test cases for the SuperStringConcatenation class

def test_default_concatenation():
    ssc = SuperStringConcatenation("Hello", "World")
    assert ssc.to_printable() == "Hello World"

def test_custom_concatenation():
    ssc = SuperStringConcatenation("Hello", "World")
    assert ssc.to_printable(sep="_") == "Hello_World"

def test_length():
    ssc = SuperStringConcatenation("Hello", "World")
    assert ssc.length() == 10

def test_character_at():
    ssc = SuperStringConcatenation("Hello", "World")
    assert ssc.character_at(7) == 'w'

def test_substring():
    ssc = SuperStringConcatenation("Hello", "World")
    assert ssc.to_printable(start=7) == "World"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringConcatenation_to_printable_0
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0.py:14:11: E1123: Unexpected keyword argument 'sep' in method call (unexpected-keyword-arg)
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0.py:26:11: E1123: Unexpected keyword argument 'start' in method call (unexpected-keyword-arg)


"""