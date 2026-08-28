# Module: pypara.dcc
import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_act_365_f

# Test cases for the "Act/365F" day count fraction calculation
def test_dcfc_act_365_f_simple_period():
    start_date = date(2007, 12, 28)
    asof_date = date(2008, 2, 28)
    end_date = asof_date
    result = dcfc_act_365_f(start=start_date, asof=asof_date, end=end_date)
    assert round(result, 14) == Decimal('0.16986301369863')

def test_dcfc_act_365_f_leap_year_period():
    start_date = date(2007, 12, 28)
    asof_date = date(2008, 2, 29)
    end_date = asof_date
    result = dcfc_act_365_f(start=start_date, asof=asof_date, end=end_date)
    assert round(result, 14) == Decimal('0.17260273972603')

def test_dcfc_act_365_f_longer_period():
    start_date = date(2007, 10, 31)
    asof_date = date(2008, 11, 30)
    end_date = asof_date
    result = dcfc_act_365_f(start=start_date, asof=asof_date, end=end_date)
    assert round(result, 14) == Decimal('1.08493150684932')

def test_dcfc_act_365_f_period_spanning_leap_year():
    start_date = date(2008, 2, 1)
    asof_date = date(2009, 5, 31)
    end_date = asof_date
    result = dcfc_act_365_f(start=start_date, asof=asof_date, end=end_date)
    assert round(result, 14) == Decimal('1.32876712328767')
