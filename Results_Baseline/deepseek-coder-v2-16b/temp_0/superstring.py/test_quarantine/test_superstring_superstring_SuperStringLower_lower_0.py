
# Module: superstring.superstring
# test_superstring.py
from superstring.superstring import SuperStringLower, ConcreteSuperString, SuperStringBase
import pytest

@pytest.fixture
def base_string():
    return "Hello World"

def test_init(base_string):
    str_lower = SuperStringLower(base_string)
    assert str_lower._base == "hello world"

def test_lower_method(base_string):
    str_lower = SuperStringLower(base_string)
    lower_str = str_lower.lower()
    assert lower_str._base == "hello world"

def test_different_base_string():
    another_str_lower = SuperStringLower("Another String")
    lower_another_str = another_str_lower.lower()
    assert lower_another_str._base == "another string"

def test_upper_method(base_string):
    str_upper = SuperStringLower(base_string)
    with pytest.raises(AttributeError):
        print(str_upper.upper())  # This should raise an AttributeError since the method is not defined

def test_character_at(base_string):
    str_lower = SuperStringLower(base_string)
    assert str_lower.character_at(2) == 'l'

def test_length():
    concrete_instance = ConcreteSuperString("Hello, World!")
    assert concrete_instance.length() == 13

def test_to_printable():
    obj = SuperStringLower(SuperStringBase("Hello, World!"))
    with pytest.raises(AttributeError):
        print(obj.to_printable(2))  # This should raise an AttributeError since the method is not defined in SuperStringLower
    with pytest.raises(AttributeError):
        print(obj.to_printable(0, 5))  # This should raise an AttributeError since the method is not defined in SuperStringLower

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringLower_lower_0
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_lower_0.py:4:0: E0611: No name 'ConcreteSuperString' in module 'superstring.superstring' (no-name-in-module)


"""