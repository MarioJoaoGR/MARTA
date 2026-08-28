
import pytest
from datetime import date, timedelta
from decimal import Decimal
from pypara.dcc import _last_payment_date

# Test 1: Monthly payments starting from January 2014 until December 31, 2015
def test_monthly_payments_start_jan_2014_end_dec_2015():
    start = date(2014, 1, 1)
    asof = date(2015, 12, 31)
    frequency = Decimal('1')
    result = _last_payment_date(start, asof, frequency)
    assert result == date(2015, 1, 1)

# Test 2: Monthly payments starting from January 2015 until December 31, 2015
def test_monthly_payments_start_jan_2015_end_dec_2015():
    start = date(2015, 1, 1)
    asof = date(2015, 12, 31)
    frequency = Decimal('1')
    result = _last_payment_date(start, asof, frequency)
    assert result == date(2015, 1, 1)

# Test 3: Bi-monthly payments starting from January 2014 until July 2015
def test_bi_monthly_payments_start_jan_2014_end_jul_2015():
    start = date(2014, 1, 1)
    asof = date(2015, 7, 1)
    frequency = Decimal('2')
    result = _last_payment_date(start, asof, frequency)
    assert result == date(2015, 7, 1)

# Test 4: Monthly payments starting from January 2014 until August 2015 with specific end of month (EOM)

# Test 5: Bi-monthly payments starting from January 2014 until April 2015 with specific end of month (EOM)
def test_bi_monthly_payments_start_jan_2014_end_apr_2015():
    start = date(2014, 1, 31)
    asof = date(2015, 4, 30)
    frequency = Decimal('2')
    eom = start.day
    result = _last_payment_date(start, asof, frequency, eom)
    assert result == date(2015, 1, 31)

# Test 6: Monthly payments starting from June 2014 until April 2015 with specific end of month (EOM)
def test_monthly_payments_start_jun_2014_end_apr_2015():
    start = date(2014, 6, 1)
    asof = date(2015, 4, 30)
    frequency = Decimal('1')
    eom = None
    result = _last_payment_date(start, asof, frequency, eom)
    assert result == date(2014, 6, 1)

# Test 7: Quarterly payments starting from July 2008 until October 2015 with specific end of month (EOM)
def test_quarterly_payments_start_jul_2008_end_oct_2015():
    start = date(2008, 7, 7)
    asof = date(2015, 10, 6)
    frequency = Decimal('3')
    eom = None
    result = _last_payment_date(start, asof, frequency, eom)
    assert result == date(2015, 7, 7)