
import pytest
from pypara.monetary import SomeMoney


def test_invalid_input():
    money = None  # Invalid instance to test error handling
    with pytest.raises(AttributeError):
        money.as_float()  # This should raise a TypeError due to invalid input