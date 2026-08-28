# Module: ansible.utils.version
# test_numeric.py
from ansible.utils.version import _Numeric

def test_numeric_initialization_with_integer():
    num1 = _Numeric(5)
    assert isinstance(num1, _Numeric), "Initialization with an integer should create an instance of _Numeric"
    assert num1.specifier == 5, "The specifier should be set to the provided integer value"

def test_numeric_initialization_with_string():
    num2 = _Numeric("6")
    assert isinstance(num2, _Numeric), "Initialization with a string should create an instance of _Numeric"
    assert num2.specifier == 6, "The specifier should be set to the integer value of the provided string"

def test_numeric_comparison():
    num1 = _Numeric(5)
    num2 = _Numeric("6")
    assert num1 < num2, "5 (as an integer) is less than 6 (as a string converted to an integer)"
    
    num3 = _Numeric("7")
    assert not (num1 == num3), "5 (as an integer) is not equal to 7 (as a string converted to an integer)"
