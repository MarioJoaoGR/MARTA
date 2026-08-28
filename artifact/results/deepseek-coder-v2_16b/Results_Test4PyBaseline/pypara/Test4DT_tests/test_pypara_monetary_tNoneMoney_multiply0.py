
import pytest
from pypara.monetary import NoneMoney

# Test cases for the multiply method of NoneMoney class
def test_multiply_with_integer():
    none_money = NoneMoney()
    result = none_money.multiply(other=10)
    assert isinstance(result, NoneMoney), "Expected an instance of NoneMoney"

def test_multiply_with_float():
    none_money = NoneMoney()
    result = none_money.multiply(other=2.5)
    assert isinstance(result, NoneMoney), "Expected an instance of NoneMoney"

def test_multiply_with_another_instance():
    none_money1 = NoneMoney()
    none_money2 = NoneMoney()
    result = none_money1.multiply(other=none_money2)