# Module: pypara.dcc
import datetime
from decimal import Decimal
import pytest

# Import the function from the module
from pypara.dcc import dcfc_30_360_german

def test_dcfc_30_360_german_basic():
    start_date = datetime.date(2007, 12, 28)
    asof_date = datetime.date(2008, 2, 28)
    end_date = datetime.date(2008, 2, 28)
    fraction = dcfc_30_360_german(start=start_date, asof=asof_date, end=end_date)
    assert round(fraction, 14) == Decimal('0.16666666666667')

def test_dcfc_30_360_german_with_leap_year():
    start_date = datetime.date(2007, 12, 28)
    asof_date = datetime.date(2008, 2, 29)
    end_date = datetime.date(2008, 2, 29)
    fraction = dcfc_30_360_german(start=start_date, asof=asof_date, end=end_date)
    assert round(fraction, 14) == Decimal('0.16944444444444')

def test_dcfc_30_360_german_month_end():
    start_date = datetime.date(2007, 10, 31)
    asof_date = datetime.date(2008, 11, 30)
    end_date = datetime.date(2008, 11, 30)
    fraction = dcfc_30_360_german(start=start_date, asof=asof_date, end=end_date)
    assert round(fraction, 14) == Decimal('1.08333333333333')

def test_dcfc_30_360_german_year_end():
    start_date = datetime.date(2008, 2, 1)
    asof_date = datetime.date(2009, 5, 31)
    end_date = datetime.date(2009, 5, 31)
    fraction = dcfc_30_360_german(start=start_date, asof=asof_date, end=end_date)
    assert round(fraction, 14) == Decimal('1.33055555555556')
