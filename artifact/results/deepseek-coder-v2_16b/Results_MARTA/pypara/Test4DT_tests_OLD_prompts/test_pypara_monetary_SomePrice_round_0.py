
import pytest
from pypara.monetary import SomePrice


def test_invalid_ndigits():
    with pytest.raises(TypeError):
        price = SomePrice(currency='USD', quantity=10.5, discount=2)
        price.round(ndigits=-1)  # Invalid ndigits should raise a TypeError