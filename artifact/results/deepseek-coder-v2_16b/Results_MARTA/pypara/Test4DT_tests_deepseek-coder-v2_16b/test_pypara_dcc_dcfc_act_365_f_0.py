
import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_act_365_f, _get_actual_day_count

def test_valid_case_1():
    ex1_start = date(2007, 12, 28)
    ex1_asof = date(2008, 2, 28)
    result1 = dcfc_act_365_f(start=ex1_start, asof=ex1_asof, end=ex1_asof)
    assert round(result1, 14) == Decimal('0.16986301369863')

def test_valid_case_2():
    ex2_start = date(2007, 12, 28)
    ex2_asof = date(2008, 2, 29)
    ex2_end = date(2008, 2, 29)
    result2 = dcfc_act_365_f(start=ex2_start, asof=ex2_asof, end=ex2_end)
    assert round(result2, 14) == Decimal('0.17260273972603')

def test_valid_case_3():
    ex3_start = date(2007, 10, 31)
    ex3_asof = date(2008, 11, 30)
    ex3_end = date(2008, 11, 30)
    result3 = dcfc_act_365_f(start=ex3_start, asof=ex3_asof, end=ex3_end)
    assert round(result3, 14) == Decimal('1.08493150684932')

def test_valid_case_4():
    ex4_start = date(2008, 2, 1)
    ex4_asof = date(2009, 5, 31)
    ex4_end = date(2009, 5, 31)
    result4 = dcfc_act_365_f(start=ex4_start, asof=ex4_asof, end=ex4_end)
    assert round(result4, 14) == Decimal('1.32876712328767')

def test_edge_case_none():
    with pytest.raises(TypeError):
        dcfc_act_365_f(start=None, asof=None, end=None)
