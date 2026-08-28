
import pytest
from pypara.monetary import SomePrice, Currency, Date

# Test for valid input scenario
def test_valid_input():
    with pytest.raises(TypeError):
        price = SomePrice(Currency('USD'), 100.50)
