
import pytest
from ansible.utils.version import _Numeric

def test_valid_case_1():
    num1 = _Numeric(5)
    assert num1.specifier == 5


def test_valid_case_3():
    num1 = _Numeric(5)
    num2 = _Numeric('10')
    assert num1 < num2, f"Expected {num1.specifier} to be less than {num2.specifier}"

def test_invalid_case_1():
    with pytest.raises(ValueError):
        num = _Numeric("abc")