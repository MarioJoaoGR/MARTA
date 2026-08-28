
import pytest
from pypara.monetary import NoneMoney, Money
from datetime import date

# Test for arithmetic operations on NoneMoney

# Test for comparison operations on NoneMoney

# Test for conversion methods on NoneMoney

# Test for Date of Valuation method on NoneMoney
def test_with_dov():
    none_money = NoneMoney()
    dov = date.today()
    result = none_money.with_dov(dov)
    assert isinstance(result, NoneMoney), "Expected a NoneMoney object but got something else"