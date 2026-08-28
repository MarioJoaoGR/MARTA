
import pytest
from pypara.monetary import NoneMoney





def test_none_money_multiplication_with_number():
    nm = NoneMoney()
    result = nm * 2
    assert isinstance(result, NoneMoney), f"Expected multiplication by 2 of an instance of NoneMoney to return another instance of NoneMoney, but got {type(result)} instead."

def test_none_money_division_with_number():
    nm = NoneMoney()
    result = nm / 1
    assert isinstance(result, NoneMoney), f"Expected division by 1 of an instance of NoneMoney to return another instance of NoneMoney, but got {type(result)} instead."

def test_none_money_floor_division_with_number():
    nm = NoneMoney()
    result = nm // 1
    assert isinstance(result, NoneMoney), f"Expected floor division by 1 of an instance of NoneMoney to return another instance of NoneMoney, but got {type(result)} instead."


def test_none_money_greater_than_comparison():
    nm = NoneMoney()
    assert not (nm > 1), "Expected greater than comparison with a number to return False"

def test_none_money_equal_comparison():
    nm = NoneMoney()
    result = nm == NoneMoney()
    assert result, "Expected equality comparison with another instance of NoneMoney to return True"