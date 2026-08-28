
import pytest
from datetime import date
from decimal import Decimal
from unittest.mock import patch, MagicMock
from pypara.dcc import dcfc_30_360_us

# Example 1: Basic usage with no frequency specified
def test_dcfc_30_360_us_basic():
    start_date = date(2007, 12, 28)
    asof_date = date(2008, 2, 28)
    end_date = date(2008, 2, 28)
    result = dcfc_30_360_us(start=start_date, asof=asof_date, end=end_date)
    assert round(result, 14) == Decimal('0.16666666666667')

# Example 2: Usage with a specific frequency (optional parameter)
def test_dcfc_30_360_us_with_freq():
    start_date = date(2007, 12, 28)
    asof_date = date(2008, 2, 29)
    end_date = date(2008, 2, 29)
    freq = Decimal('0.5')
    result = dcfc_30_360_us(start=start_date, asof=asof_date, end=end_date, freq=freq)
    assert round(result, 14) == Decimal('0.16944444444444')

# Example 3: Handling the last day of a month by specifying the 'asof' date
def test_dcfc_30_360_us_last_day():
    start_date = date(2007, 10, 31)
    asof_date = date(2008, 11, 30)
    end_date = date(2008, 11, 30)
    result = dcfc_30_360_us(start=start_date, asof=asof_date, end=end_date)
    assert round(result, 14) == Decimal('1.08333333333333')

# Example 4: Handling the last day of a month by specifying the 'asof' date with different dates
def test_dcfc_30_360_us_different_dates():
    start_date = date(2008, 2, 1)
    asof_date = date(2009, 5, 31)
    end_date = date(2009, 5, 31)
    result = dcfc_30_360_us(start=start_date, asof=asof_date, end=end_date)
    assert round(result, 14) == Decimal('1.33333333333333')
