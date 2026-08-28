
import pytest
from datetime import date
from decimal import Decimal
from unittest.mock import patch
from pypara.dcc import _last_payment_date, _construct_date

# Test 1: Monthly payments starting from January 2014 until December 31, 2015
def test_monthly_payments_jan_to_dec():
    start_date = date(2014, 1, 1)
    asof_date = date(2015, 12, 31)
    frequency = Decimal('1')
    with patch('pypara.dcc._construct_date', return_value=date(2015, 1, 1)):
        result = _last_payment_date(start_date, asof_date, frequency)
        assert result == date(2015, 1, 1)

# Test 2: Monthly payments starting from January 2015 until December 31, 2015
def test_monthly_payments_jan_to_dec_2():
    start_date = date(2015, 1, 1)
    asof_date = date(2015, 12, 31)
    frequency = Decimal('1')
    with patch('pypara.dcc._construct_date', return_value=date(2015, 1, 1)):
        result = _last_payment_date(start_date, asof_date, frequency)
        assert result == date(2015, 1, 1)

# Test 3: Bi-monthly payments starting from January 2014 until July 2015
def test_bi_monthly_payments():
    start_date = date(2014, 1, 1)
    asof_date = date(2015, 7, 1)
    frequency = Decimal('2')
    with patch('pypara.dcc._construct_date', return_value=date(2015, 7, 1)):
        result = _last_payment_date(start_date, asof_date, frequency)
        assert result == date(2015, 7, 1)

# Test 4: Monthly payments starting from January 2014 until August 2015 with specific end of month (EOM)
def test_monthly_payments_with_eom():
    start_date = date(2014, 1, 31)
    asof_date = date(2015, 8, 31)
    frequency = Decimal('1')
    eom = start_date.day
    with patch('pypara.dcc._construct_date', return_value=date(2015, 7, 31)):
        result = _last_payment_date(start_date, asof_date, frequency, eom)
        assert result == date(2015, 7, 31)

# Test 5: Bi-monthly payments starting from January 2014 until April 2015 with specific end of month (EOM)
def test_bi_monthly_payments_with_eom():
    start_date = date(2014, 1, 31)
    asof_date = date(2015, 4, 30)
    frequency = Decimal('2')
    eom = start_date.day
    with patch('pypara.dcc._construct_date', return_value=date(2015, 1, 31)):
        result = _last_payment_date(start_date, asof_date, frequency, eom)
        assert result == date(2015, 1, 31)

# Test 6: Monthly payments starting from June 2014 until April 2015 with specific end of month (EOM)
def test_monthly_payments_without_eom():
    start_date = date(2014, 6, 1)
    asof_date = date(2015, 4, 30)
    frequency = Decimal('1')
    eom = None
    with patch('pypara.dcc._construct_date', return_value=date(2014, 6, 1)):
        result = _last_payment_date(start_date, asof_date, frequency, eom)
        assert result == date(2014, 6, 1)

# Test 7: Quarterly payments starting from July 2008 until October 2015 with specific end of month (EOM)
def test_quarterly_payments():
    start_date = date(2008, 7, 7)
    asof_date = date(2015, 10, 6)
    frequency = Decimal('3')
    eom = None
    with patch('pypara.dcc._construct_date', return_value=date(2015, 7, 7)):
        result = _last_payment_date(start_date, asof_date, frequency, eom)
        assert result == date(2015, 7, 7)
