
import pytest
from datetime import date
from decimal import Decimal
import pypara.dcc as dcc

# Example 1: Basic call with month-end dates
def test_dcfc_30_360_isda_basic():
    ex1_start = date(2007, 12, 28)
    ex1_asof = date(2008, 2, 28)
    result1 = dcc.dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof)
    assert round(result1, 4) == Decimal('0.1667')

# Example 2: Call with a leap year date
def test_dcfc_30_360_isda_leap_year():
    ex2_start = date(2007, 12, 28)
    ex2_asof = date(2008, 2, 29)
    result2 = dcc.dcfc_30_360_isda(start=ex2_start, asof=ex2_asof, end=ex2_asof)
    assert round(result2, 4) == Decimal('0.1694')

# Example 3: Call with specific month end dates
def test_dcfc_30_360_isda_specific_month_end():
    ex3_start = date(2007, 10, 31)
    ex3_asof = date(2008, 11, 30)
    result3 = dcc.dcfc_30_360_isda(start=ex3_start, asof=ex3_asof, end=ex3_asof)
    assert round(result3, 4) == Decimal('1.0833')

# Example 4: Call with a longer period including a leap year
def test_dcfc_30_360_isda_longer_period():
    ex4_start = date(2008, 2, 1)
    ex4_asof = date(2009, 5, 31)
    result4 = dcc.dcfc_30_360_isda(start=ex4_start, asof=ex4_asof, end=ex4_asof)
    assert round(result4, 4) == Decimal('1.3333')

# Additional test case to check the function with a normal date scenario
def test_dcfc_30_360_isda_normal_date():
    ex5_start = date(2008, 1, 1)
    ex5_asof = date(2008, 1, 31)
    result5 = dcc.dcfc_30_360_isda(start=ex5_start, asof=ex5_asof, end=ex5_asof)
    assert round(result5, 4) == Decimal('0.0833')

# Test case to check the function when both start and asof are 31
def test_dcfc_30_360_isda_both_dates_31():
    ex6_start = date(2007, 12, 31)
    ex6_asof = date(2008, 12, 31)
    result6 = dcc.dcfc_30_360_isda(start=ex6_start, asof=ex6_asof, end=ex6_asof)