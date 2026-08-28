
import pytest
from datetime import date, timedelta
from decimal import Decimal
from unittest.mock import patch
from pypara.dcc import _last_payment_date, _construct_date  # Assuming the function and module are in this namespace

def test_valid_inputs():
    with patch('pypara.dcc._last_payment_date', autospec=True):
        start = date(2014, 1, 1)
        asof = date(2015, 12, 31)
        frequency = Decimal('1')
        result = _last_payment_date(start, asof, frequency)
        assert result == date(2015, 1, 1), f"Expected date(2015, 1, 1), but got {result}"

def test_edge_cases():
    with patch('pypara.dcc._last_payment_date', autospec=True):
        start = date(2014, 1, 1)
        asof = date(2015, 12, 31)
        frequency = Decimal('1')
        result = _last_payment_date(start, asof, frequency)
        assert result == date(2015, 1, 1), f"Expected date(2015, 1, 1), but got {result}"

def test_invalid_inputs():
    with patch('pypara.dcc._last_payment_date', autospec=True):
        start = date(2014, 1, 1)
        asof = date(2015, 12, 31)
        frequency = Decimal('1')
        result = _last_payment_date(start, asof, frequency)
        assert result == date(2015, 1, 1), f"Expected date(2015, 1, 1), but got {result}"
