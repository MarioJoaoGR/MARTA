
import pytest
from decimal import Decimal
from datetime import date, timedelta
from unittest.mock import patch
from pypara.monetary import SomePrice



def test_arithmetic_operations():
    with pytest.raises(TypeError):
        price1 = SomePrice(ccy='USD', qty=Decimal('50'))

def test_comparison_operators():
    with pytest.raises(TypeError):
        price1 = SomePrice(ccy='USD', qty=Decimal('100'))