# Module: pypara.dcc
import datetime
from decimal import Decimal
import pytest
from pypara.dcc import dcfc_nl_365

# Test cases for the dcfc_nl_365 function
def test_dcfc_nl_365_simple():
    start_date = datetime.date(2007, 12, 28)
    asof_date = datetime.date(2008, 2, 28)
    end_date = datetime.date(2008, 2, 28)
    fraction = dcfc_nl_365(start=start_date, asof=asof_date, end=end_date)
    assert round(fraction, 14) == Decimal('0.16986301369863')

def test_dcfc_nl_365_leap_day():
    start_date = datetime.date(2007, 12, 28)
    asof_date = datetime.date(2008, 2, 29)
    end_date = datetime.date(2008, 2, 29)
    fraction = dcfc_nl_365(start=start_date, asof=asof_date, end=end_date)
    assert round(fraction, 14) == Decimal('0.16986301369863')

def test_dcfc_nl_365_longer_period():
    start_date = datetime.date(2007, 10, 31)
    asof_date = datetime.date(2008, 11, 30)
    end_date = datetime.date(2008, 11, 30)
    fraction = dcfc_nl_365(start=start_date, asof=asof_date, end=end_date)
    assert round(fraction, 14) == Decimal('1.08219178082192')

def test_dcfc_nl_365_year_long_period():
    start_date = datetime.date(2008, 2, 1)
    asof_date = datetime.date(2009, 5, 31)
    end_date = datetime.date(2009, 5, 31)
    fraction = dcfc_nl_365(start=start_date, asof=asof_date, end=end_date)
    assert round(fraction, 14) == Decimal('1.32602739726027')

# Add more test cases if needed to cover different scenarios or edge cases
