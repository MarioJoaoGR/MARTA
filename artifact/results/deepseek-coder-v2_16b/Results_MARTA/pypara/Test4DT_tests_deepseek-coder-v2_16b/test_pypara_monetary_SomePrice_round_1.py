
import pytest
from pypara.monetary import SomePrice



def test_undefined_quantity():
    with pytest.raises(TypeError):
        price = SomePrice(currency='USD', quantity=None, discount=2)
        price.round()