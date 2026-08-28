# Module: pypara.dcc
import datetime
from decimal import Decimal
import pytest

# Import the function correctly using its module name
from pypara.dcc import dcfc_30_e_plus_360

def test_dcfc_30_e_plus_360_basic():
    ex1_start = datetime.date(2007, 12, 28)
    ex1_asof = datetime.date(2008, 2, 28)
    result1 = dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof)
    assert round(result1, 14) == Decimal('0.16666666666667')

def test_dcfc_30_e_plus_360_with_freq():
    ex2_start = datetime.date(2007, 12, 28)
    ex2_asof = datetime.date(2008, 2, 29)
    result2 = dcfc_30_e_plus_360(start=ex2_start, asof=ex2_asof, end=ex2_asof, freq=Decimal('1'))
    assert round(result2, 14) == Decimal('0.16944444444444')

def test_dcfc_30_e_plus_360_adjust_day():
    ex3_start = datetime.date(2007, 10, 31)
    ex3_asof = datetime.date(2008, 11, 30)
    result3 = dcfc_30_e_plus_360(start=ex3_start, asof=ex3_asof, end=ex3_asof)
    assert round(result3, 14) == Decimal('1.08333333333333')

def test_dcfc_30_e_plus_360_long_period():
    ex4_start = datetime.date(2008, 2, 1)
    ex4_asof = datetime.date(2009, 5, 31)
    result4 = dcfc_30_e_plus_360(start=ex4_start, asof=ex4_asof, end=ex4_asof)
    assert round(result4, 14) == Decimal('1.33333333333333')

# Add more test cases if necessary to cover all edge cases and scenarios
