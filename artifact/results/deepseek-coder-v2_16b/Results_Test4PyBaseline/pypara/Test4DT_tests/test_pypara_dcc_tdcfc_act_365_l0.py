# Module: pypara.dcc
import datetime
from decimal import Decimal
import pytest
import calendar

# Import the function from the module
from pypara.dcc import dcfc_act_365_l

def test_dcfc_act_365_l_standard_year():
    start_date = datetime.date(2007, 12, 28)
    asof_date = datetime.date(2008, 2, 28)
    end_date = datetime.date(2008, 2, 28)
    fraction = dcfc_act_365_l(start=start_date, asof=asof_date, end=end_date)
    assert round(fraction, 14) == Decimal('0.16939890710383')

def test_dcfc_act_365_l_leap_year():
    start_date = datetime.date(2007, 12, 28)
    asof_date = datetime.date(2008, 2, 29)
    end_date = datetime.date(2008, 2, 29)
    fraction = dcfc_act_365_l(start=start_date, asof=asof_date, end=end_date)
    assert round(fraction, 14) == Decimal('0.17213114754098')

def test_dcfc_act_365_l_multiple_months():
    start_date = datetime.date(2007, 10, 31)
    asof_date = datetime.date(2008, 11, 30)
    end_date = datetime.date(2008, 11, 30)
    fraction = dcfc_act_365_l(start=start_date, asof=asof_date, end=end_date)
    assert round(fraction, 14) == Decimal('1.08196721311475')

def test_dcfc_act_365_l_year_span():
    start_date = datetime.date(2008, 2, 1)
    asof_date = datetime.date(2009, 5, 31)
    end_date = datetime.date(2009, 5, 31)
    fraction = dcfc_act_365_l(start=start_date, asof=asof_date, end=end_date)
    assert round(fraction, 14) == Decimal('1.32876712328767')

def test_dcfc_act_365_l_with_invalid_dates():
    # Invalid dates should raise an error or return a meaningful result indicating the issue
    with pytest.raises(Exception):  # Assuming the function raises an exception for invalid dates
        start_date = datetime.date(2007, 13, 1)  # December is 12th month
        asof_date = datetime.date(2008, 2, 29)
        end_date = datetime.date(2008, 3, 1)
        dcfc_act_365_l(start=start_date, asof=asof_date, end=end_date)
