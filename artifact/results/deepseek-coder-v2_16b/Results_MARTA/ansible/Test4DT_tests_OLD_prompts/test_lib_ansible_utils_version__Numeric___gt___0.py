
import pytest
from ansible.utils.version import _Numeric

def test_non_numeric_characters():
    with pytest.raises(ValueError):
        num = _Numeric("abc")

def test_invalid_version_string():
    with pytest.raises(ValueError):
        num = _Numeric("123abc")

def test_valid_integer():
    num = _Numeric(123)
    assert isinstance(num, _Numeric)
    assert num.specifier == 123

def test_valid_string():
    num = _Numeric("123")
    assert isinstance(num, _Numeric)
    assert num.specifier == 123

def test_greater_than():
    num1 = _Numeric(50)
    num2 = _Numeric(49)
    assert num1 > num2

def test_not_greater_than():
    num1 = _Numeric(30)
    num2 = _Numeric(31)
    assert not (num1 > num2)
