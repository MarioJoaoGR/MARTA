
import pytest
from pypara.monetary import NonePrice, Price

def test_valid_case():
    none_price = NonePrice()
    another_none_price = NonePrice()
    
    assert none_price.lte(another_none_price) == True
    assert none_price == another_none_price
