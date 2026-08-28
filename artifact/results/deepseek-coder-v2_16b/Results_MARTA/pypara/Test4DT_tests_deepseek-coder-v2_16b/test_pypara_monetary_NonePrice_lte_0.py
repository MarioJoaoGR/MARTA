
import pytest
from pypara.monetary import NonePrice

def test_none_price_comparison():
    none_price = NonePrice()
    another_none_price = NonePrice()
    
    # Comparing two instances of NonePrice should always return True
    assert none_price.lte(another_none_price) == True


def test_none_price_conversion():
    none_price = NonePrice()
    
    # Converting an instance of NonePrice to float or int should raise TypeError
    with pytest.raises(TypeError):
        float_value = float(none_price)