
import pytest
from pypara.monetary import NoneMoney

# Test case for dividing a predefined NoneMoney object by a numeric value
def test_divide_none_money_by_numeric():
    money = NoneMoney()
    result = money.divide(2)
    assert isinstance(result, NoneMoney), "Expected the same type of object to be returned"