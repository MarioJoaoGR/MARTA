
import pytest
from unittest.mock import patch
from pypara.monetary import NonePrice, NoMoney

# Test for float conversion of NonePrice
def test_noneprice_float_conversion():
    np = NonePrice()
    with pytest.raises(TypeError) as excinfo:
        float(np)
    assert str(excinfo.value) == "Undefined monetary values do not have quantity information."

# Test for int conversion of NonePrice
def test_noneprice_int_conversion():
    np = NonePrice()
    with pytest.raises(TypeError) as excinfo:
        int(np)
    assert str(excinfo.value) == "Undefined monetary values do not have quantity information."

# Test for less than comparison of NonePrice

# Test for less than or equal to comparison of NonePrice

# Test for greater than comparison of NonePrice

# Test for greater than or equal to comparison of NonePrice