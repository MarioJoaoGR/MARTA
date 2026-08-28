
import pytest
from decimal import Decimal
from datetime import date, timedelta
from unittest.mock import patch
from pypara.dcc import _last_payment_date


def test_monthly_payments():
    start = date(2014, 1, 31)
    asof = date(2015, 12, 31)
    frequency = Decimal('1')
    
    with patch('pypara.dcc._construct_date', return_value=date(2015, 1, 31)):
        result = _last_payment_date(start, asof, frequency)
        assert result == date(2015, 1, 31)

def test_bi_monthly_payments():
    start = date(2014, 1, 31)
    asof = date(2015, 7, 31)
    frequency = Decimal('2')
    
    with patch('pypara.dcc._construct_date', return_value=date(2015, 1, 31)):
        result = _last_payment_date(start, asof, frequency)
        assert result == date(2015, 1, 31)

def test_quarterly_payments():
    start = date(2008, 7, 7)
    asof = date(2015, 7, 7)
    frequency = Decimal('3')
    
    with patch('pypara.dcc._construct_date', return_value=date(2015, 7, 7)):
        result = _last_payment_date(start, asof, frequency)
        assert result == date(2015, 7, 7)

def test_monthly_payments_specific_eom():
    start = date(2014, 1, 31)
    asof = date(2015, 8, 31)
    frequency = Decimal('1')
    eom = 31
    
    with patch('pypara.dcc._construct_date', return_value=date(2015, 7, 31)):
        result = _last_payment_date(start, asof, frequency, eom)
        assert result == date(2015, 7, 31)

def test_bi_monthly_payments_specific_eom():
    start = date(2014, 1, 31)
    asof = date(2015, 4, 30)
    frequency = Decimal('2')
    eom = 31
    
    with patch('pypara.dcc._construct_date', return_value=date(2015, 1, 31)):
        result = _last_payment_date(start, asof, frequency, eom)
        assert result == date(2015, 1, 31)

def test_monthly_payments_specific_start():
    start = date(2014, 6, 1)
    asof = date(2015, 4, 30)
    frequency = Decimal('1')
    
    with patch('pypara.dcc._construct_date', return_value=date(2014, 6, 1)):
        result = _last_payment_date(start, asof, frequency)
        assert result == date(2014, 6, 1)