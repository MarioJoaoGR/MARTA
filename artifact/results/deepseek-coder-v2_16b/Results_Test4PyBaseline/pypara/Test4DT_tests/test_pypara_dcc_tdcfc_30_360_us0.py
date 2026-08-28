# Module: pypara.dcc
import datetime
from decimal import Decimal
import pytest

# Import the function from the module
from pypara.dcc import dcfc_30_360_us

def test_dcfc_30_360_us_simple():
    ex1_start = datetime.date(2007, 12, 28)
    ex1_asof = datetime.date(2008, 2, 28)
    result = dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof)
    assert round(result, 14) == Decimal('0.16666666666667')

def test_dcfc_30_360_us_leap_year():
    ex2_start = datetime.date(2007, 12, 28)
    ex2_asof = datetime.date(2008, 2, 29)
    result = dcfc_30_360_us(start=ex2_start, asof=ex2_asof, end=ex2_asof)
    assert round(result, 14) == Decimal('0.16944444444444')

def test_dcfc_30_360_us_end_of_month():
    ex3_start = datetime.date(2007, 10, 31)
    ex3_asof = datetime.date(2008, 11, 30)
    result = dcfc_30_360_us(start=ex3_start, asof=ex3_asof, end=ex3_asof)
    assert round(result, 14) == Decimal('1.08333333333333')

def test_dcfc_30_360_us_multiple_months():
    ex4_start = datetime.date(2008, 2, 1)
    ex4_asof = datetime.date(2009, 5, 31)
    result = dcfc_30_360_us(start=ex4_start, asof=ex4_asof, end=ex4_asof)
    assert round(result, 14) == Decimal('1.33333333333333')

# Add more test cases if necessary to cover all edge cases and scenarios
