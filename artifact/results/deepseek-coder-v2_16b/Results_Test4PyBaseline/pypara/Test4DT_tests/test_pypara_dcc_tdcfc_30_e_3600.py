# Module: pypara.dcc
import datetime
from decimal import Decimal
import pytest

# Import the function from its module
from pypara.dcc import dcfc_30_e_360

def test_dcfc_30_e_360_normal_month():
    ex1_start = datetime.date(2007, 12, 28)
    ex1_asof = datetime.date(2008, 2, 28)
    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

def test_dcfc_30_e_360_leap_year():
    ex2_start = datetime.date(2007, 12, 28)
    ex2_asof = datetime.date(2008, 2, 29)
    assert round(dcfc_30_e_360(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16944444444444')

def test_dcfc_30_e_360_adjust_start():
    ex3_start = datetime.date(2007, 10, 31)
    ex3_asof = datetime.date(2008, 11, 30)
    assert round(dcfc_30_e_360(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08333333333333')

def test_dcfc_30_e_360_multiple_months():
    ex4_start = datetime.date(2008, 2, 1)
    ex4_asof = datetime.date(2009, 5, 31)
    assert round(dcfc_30_e_360(start=ex4_start, asof=ex4_asof, end=ex4_asof), 14) == Decimal('1.33055555555556')

if __name__ == "__main__":
    pytest.main()
