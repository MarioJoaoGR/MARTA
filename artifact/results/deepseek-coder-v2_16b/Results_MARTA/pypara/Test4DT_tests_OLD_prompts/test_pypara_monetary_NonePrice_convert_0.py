
import pytest
from unittest.mock import patch
from pypara.monetary import Currency, NonePrice, Price
from datetime import date as Date

def test_valid_inputs():
    price = NonePrice()
    with pytest.raises(TypeError):
        currency = Currency('USD')

