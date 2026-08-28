
import pytest
from pypara.monetary import NonePrice

def test_noneprice_initialization():
    undefined_price = NonePrice()
    assert isinstance(undefined_price, NonePrice), "Initialization should create an instance of NonePrice"

def test_noneprice_round_default():
    undefined_price = NonePrice()
    rounded_price = undefined_price.round()
    assert isinstance(rounded_price, NonePrice), "Default rounding should return an instance of NonePrice"
    assert rounded_price is undefined_price, "Rounding an undefined price should not change the object"

def test_noneprice_round_with_digits():
    undefined_price = NonePrice()
    rounded_price = undefined_price.round(ndigits=2)
    assert isinstance(rounded_price, NonePrice), "Rounding with specified digits should return an instance of NonePrice"
    assert rounded_price is undefined_price, "Rounding to a specific number of digits should not change the object"
