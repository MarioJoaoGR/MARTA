
import pytest
from unittest.mock import patch, MagicMock
from pypara.dcc import dcfc_30_e_plus_360
import datetime
from decimal import Decimal


def test_valid_dates():
    ex1_start = datetime.date(2007, 12, 28)
    ex1_asof = datetime.date(2008, 2, 28)
    result = dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof)
    assert round(result, 14) == Decimal('0.16666666666667')

def test_valid_dates_with_leap_year():
    ex2_start = datetime.date(2007, 12, 28)
    ex2_asof = datetime.date(2008, 2, 29)
    result = dcfc_30_e_plus_360(start=ex2_start, asof=ex2_asof, end=ex2_asof)
    assert round(result, 14) == Decimal('0.16944444444444')

def test_dates_with_month_end():
    ex3_start = datetime.date(2007, 10, 31)
    ex3_asof = datetime.date(2008, 11, 30)
    result = dcfc_30_e_plus_360(start=ex3_start, asof=ex3_asof, end=ex3_asof)
    assert round(result, 14) == Decimal('1.08333333333333')

def test_long_period():
    ex4_start = datetime.date(2008, 2, 1)
    ex4_asof = datetime.date(2009, 5, 31)
    result = dcfc_30_e_plus_360(start=ex4_start, asof=ex4_asof, end=ex4_asof)
    assert round(result, 14) == Decimal('1.33333333333333')