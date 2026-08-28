
import pytest
from pypara.monetary import NonePrice

# Test initialization of NonePrice instance
def test_noneprice_initialization():
    undefined_price = NonePrice()
    assert isinstance(undefined_price, NonePrice), "Instance should be an instance of NonePrice"