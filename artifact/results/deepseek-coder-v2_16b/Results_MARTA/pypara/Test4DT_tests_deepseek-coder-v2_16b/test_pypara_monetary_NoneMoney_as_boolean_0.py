
import pytest
from pypara.monetary import NoneMoney

# Test 1: Initialize a NoneMoney object and check its boolean value
def test_none_money_bool():
    nm = NoneMoney()
    assert bool(nm) is False, "NoneMoney should evaluate to False in a boolean context"

# Test 2: Compare two undefined NoneMoney objects
def test_none_money_comparison():
    money1 = NoneMoney()
    money2 = NoneMoney()
    assert money1 == money2, "Two undefined NoneMoney objects should be considered equal"

# Test 3: Attempt to convert a NoneMoney object and handle TypeError
def test_none_money_conversion():
    with pytest.raises(TypeError) as excinfo:
        float(NoneMoney())
    assert str(excinfo.value) == "Undefined monetary values do not have quantity information.", \
           "Converting NoneMoney to float should raise a TypeError with the correct message"
