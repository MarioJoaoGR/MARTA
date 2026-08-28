
import pytest
from datetime import date
from decimal import Decimal
from unittest.mock import patch
from pypara.dcc import dcfc_30_360_us

def test_valid_case_1():
    start_date = date(2007, 12, 28)
    asof_date = date(2008, 2, 28)
    end_date = date(2008, 2, 28)
    with patch('pypara.dcc._is_last_day_of_month', return_value=False):
        result = dcfc_30_360_us(start=start_date, asof=asof_date, end=end_date)
        assert round(result, 14) == Decimal('0.16666666666667')

def test_valid_case_2():
    start_date = date(2007, 12, 28)
    asof_date = date(2008, 2, 29)
    end_date = date(2008, 2, 29)
    with patch('pypara.dcc._is_last_day_of_month', return_value=False):
        result = dcfc_30_360_us(start=start_date, asof=asof_date, end=end_date)
        assert round(result, 14) == Decimal('0.16944444444444')

def test_valid_case_3():
    start_date = date(2007, 10, 31)
    asof_date = date(2008, 11, 30)
    end_date = date(2008, 11, 30)
    with patch('pypara.dcc._is_last_day_of_month', return_value=False):
        result = dcfc_30_360_us(start=start_date, asof=asof_date, end=end_date)
        assert round(result, 14) == Decimal('1.08333333333333')

def test_valid_case_4():
    start_date = date(2008, 2, 1)
    asof_date = date(2009, 5, 31)
    end_date = date(2009, 5, 31)
    with patch('pypara.dcc._is_last_day_of_month', return_value=False):
        result = dcfc_30_360_us(start=start_date, asof=asof_date, end=end_date)
        assert round(result, 14) == Decimal('1.33333333333333')
