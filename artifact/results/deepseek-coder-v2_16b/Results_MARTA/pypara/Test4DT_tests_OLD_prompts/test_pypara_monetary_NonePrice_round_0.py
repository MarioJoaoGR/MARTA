
import pytest
from pypara.monetary import NonePrice

def test_noneprice_round_default():
    undefined_price = NonePrice()
    rounded_price = undefined_price.round()
    assert isinstance(rounded_price, NonePrice), "Expected an instance of NonePrice"

def test_noneprice_round_with_digits():
    undefined_price = NonePrice()
    rounded_price_with_digits = undefined_price.round(ndigits=2)
    assert isinstance(rounded_price_with_digits, NonePrice), "Expected an instance of NonePrice"
