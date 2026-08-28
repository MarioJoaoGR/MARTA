
import pytest
from datetime import date
from decimal import Decimal
import pypara.dcc as dcc

# Test Case 1: Start date's day is not 31
def test_dcfc_30_360_isda_start_not_31():
    ex1_start = date(2007, 12, 28)
    ex1_asof = date(2008, 2, 28)
    result = dcc.dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof)
    assert round(result, 14) == Decimal('0.16666666666667')

# Test Case 2: Start and asof dates' days are both 30, but end date's day is 31
def test_dcfc_30_360_isda_start_and_asof_30_end_31():
    ex2_start = date(2007, 12, 28)
    ex2_asof = date(2008, 2, 29)
    result = dcc.dcfc_30_360_isda(start=ex2_start, asof=ex2_asof, end=ex2_asof)
    assert round(result, 14) == Decimal('0.16944444444444')

# Test Case 3: Start date's day is 31 (adjusted to 30), end and asof dates are the same but not 31
def test_dcfc_30_360_isda_start_31_end_and_asof_same():
    ex3_start = date(2007, 10, 31)
    ex3_asof = date(2008, 11, 30)
    result = dcc.dcfc_30_360_isda(start=ex3_start, asof=ex3_asof, end=ex3_asof)
    assert round(result, 14) == Decimal('1.08333333333333')

# Test Case 4: Start and asof dates are not the same but follow the adjustment rules
def test_dcfc_30_360_isda_adjustment():
    ex4_start = date(2008, 2, 1)
    ex4_asof = date(2009, 5, 31)
    result = dcc.dcfc_30_360_isda(start=ex4_start, asof=ex4_asof, end=ex4_asof)
    assert round(result, 14) == Decimal('1.33333333333333')
