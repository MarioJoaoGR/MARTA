
import pytest
from pypara.monetary import NonePrice, NoMoney

# Test 1: Creating an instance of NonePrice
def test_create_noneprice():
    price = NonePrice()
    assert isinstance(price, NonePrice)
    assert bool(price) is False

# Test 2: Comparing two instances of NonePrice
def test_compare_noneprice():
    price1 = NonePrice()
    price2 = NonePrice()
    assert price1 == price2

# Test 3: Performing arithmetic operations with NonePrice

# Test 4: Converting NonePrice to float or int
def test_convert_noneprice():
    price = NonePrice()
    with pytest.raises(TypeError):
        float(price)
    with pytest.raises(TypeError):
        int(price)

# Test 5: Adding a defined Price object to an undefined NonePrice