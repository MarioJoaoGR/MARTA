
import pytest
from decimal import Decimal
from datetime import date
from pypara.monetary import Currency, Price, NoPrice  # Assuming this is a valid module from pypara



def test_create_price_with_missing_parameters():
    with pytest.raises(TypeError):
        Price.of(Currency('USD'), None, date(2023, 4, 1))
