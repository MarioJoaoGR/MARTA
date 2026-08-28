
import pytest
from pypara.monetary import SomePrice

# Test for defined instances comparison

# Test for undefined instances comparison (None)
def test_is_equal_undefined():
    price1 = None
    price2 = None
    with pytest.raises(AttributeError):
        assert price1.is_equal(price2) == True

# Test for different class comparison