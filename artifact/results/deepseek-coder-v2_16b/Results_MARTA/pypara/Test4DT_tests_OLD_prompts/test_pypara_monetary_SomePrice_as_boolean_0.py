
import pytest
from unittest.mock import patch, MagicMock
from decimal import Decimal
from datetime import date
from pypara.monetary import SomePrice

def test_valid_input():
    with patch('pypara.monetary.SomePrice', autospec=True) as mock_price:
        mock_price.return_value = MagicMock()
        mock_price.return_value.qty = Decimal('100.25')
        
        price = SomePrice(ccy='USD', qty=Decimal('100.25'), dov=date.today())
        assert bool(price) is True, "Expected the price to be defined"
