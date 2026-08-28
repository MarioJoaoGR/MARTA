
import datetime
from decimal import Decimal
import pytest
from unittest.mock import patch
from pypara.dcc import dcfc_30_360_isda

# Test function for the "30/360 ISDA" day count fraction calculation
def test_dcfc_30_360_isda():
    # Example 1: Start date's day is not 31
    ex1_start = datetime.date(2007, 12, 28)
    ex1_asof = datetime.date(2008, 2, 28)
    result1 = dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof)
    assert round(result1, 14) == Decimal('0.16666666666667')

    # Example 2: Start and asof dates' days are both 30, but end date's day is 31
    ex2_start = datetime.date(2007, 12, 28)
    ex2_asof = datetime.date(2008, 2, 29)
    result2 = dcfc_30_360_isda(start=ex2_start, asof=ex2_asof, end=ex2_asof)
    assert round(result2, 14) == Decimal('0.16944444444444')

    # Example 3: Start date's day is 31 (adjusted to 30), end and asof dates are the same but not 31
    ex3_start = datetime.date(2007, 10, 31)
    ex3_asof = datetime.date(2008, 11, 30)
    result3 = dcfc_30_360_isda(start=ex3_start, asof=ex3_asof, end=ex3_asof)
    assert round(result3, 14) == Decimal('1.08333333333333')

    # Example 4: Start and asof dates are not the same but follow the adjustment rules
    ex4_start = datetime.date(2008, 2, 1)
    ex4_asof = datetime.date(2009, 5, 31)
    result4 = dcfc_30_360_isda(start=ex4_start, asof=ex4_asof, end=ex4_asof)
    assert round(result4, 14) == Decimal('1.33333333333333')
