
# Module: superstring.superstring
import pytest
from superstring.superstring import SuperStringBase, SuperString, SuperStringUpper, MyString, SuperStringConcatenation

# Test cases for SuperStringBase class
def test_SuperStringBase_add_with_SuperString():
    s1 = SuperStringBase("Hello")
    result = s1 + " World"
    assert str(result) == "Hello World"

def test_SuperStringBase_add_with_non_SuperString():
    s1 = SuperStringBase("Hello")
    result = s1 + MyString(" World")
    assert str(result) == "Hello World"

# Test cases for SuperString class
def test_SuperString_length():
    s = SuperString("Hello, World!")
    assert s.length() == 13

def test_SuperString_to_printable():
    s = SuperString("Hello, World!")
    assert s.to_printable() == "Hello, World!"
    assert s.to_printable(start_index=7) == "World!"
    assert s.to_printable(end_index=5) == "Hello"

def test_SuperString_character_at():
    s = SuperString("Hello, World!")
    assert s.character_at(0) == 'H'
    assert s.character_at(4) == 'o'

# Test cases for SuperStringUpper class
def test_SuperStringUpper_upper():
    s = SuperStringUpper("hello world")
    result = s.upper()
    assert str(result._base) == "HELLO WORLD"

def test_SuperStringUpper_lower():
    s = SuperStringUpper("HELLO WORLD")
    result = s.lower()
    assert str(result._base) == "hello world"

# Test cases for MyString class (subclass of SuperStringBase)
def test_MyString_length():
    my_string = MyString("Hello, World!")
    assert my_string.length() == 13

def test_MyString_character_at():
    my_string = MyString("Hello, World!")
    assert my_string.character_at(7) == 'W'

# Test cases for SuperStringConcatenation class
def test_SuperStringConcatenation_str():
    s1 = SuperStringBase("Hello")
    result = s1 + " World"
    assert str(result) == "Hello World"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringBase___add___0
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___add___0.py:4:0: E0611: No name 'MyString' in module 'superstring.superstring' (no-name-in-module)


"""