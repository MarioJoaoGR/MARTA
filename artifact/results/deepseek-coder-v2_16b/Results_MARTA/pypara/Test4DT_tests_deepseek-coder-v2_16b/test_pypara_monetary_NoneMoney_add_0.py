
import pytest
from pypara.monetary import NoneMoney

# Scenario 1: Initialize a NoneMoney Instance
def test_initialize_NoneMoney():
    nm = NoneMoney()
    assert isinstance(nm, NoneMoney)

# Scenario 2: Add Two Undefined Money Objects
def test_add_undefined_money():
    money1 = NoneMoney()
    money2 = NoneMoney()
    result_add = money1 + money2
    assert isinstance(result_add, NoneMoney)

# Scenario 3: Compare Two Undefined Money Objects
def test_compare_undefined_money():
    money1 = NoneMoney()
    money2 = NoneMoney()
    assert money1 == money2

# Scenario 4: Convert Undefined Money to Float (Raises TypeError)
def test_convert_undefined_money_to_float():
    with pytest.raises(TypeError):
        float(NoneMoney())
