
import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_30_360_isda

def test_dcfc_30_360_isda_example1():
    ex1_start = date(2007, 12, 28)
    ex1_asof = date(2008, 2, 28)
    result = dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof)
    assert round(result, 14) == Decimal('0.16666666666667')

def test_dcfc_30_360_isda_example2():
    ex2_start = date(2007, 12, 28)
    ex2_asof = date(2008, 2, 29)
    result = dcfc_30_360_isda(start=ex2_start, asof=ex2_asof, end=ex2_asof)
    assert round(result, 14) == Decimal('0.16944444444444')

def test_dcfc_30_360_isda_example3():
    ex3_start = date(2007, 10, 31)
    ex3_asof = date(2008, 11, 30)
    result = dcfc_30_360_isda(start=ex3_start, asof=ex3_asof, end=ex3_asof)
    assert round(result, 14) == Decimal('1.08333333333333')

def test_dcfc_30_360_isda_example4():
    ex4_start = date(2008, 2, 1)
    ex4_asof = date(2009, 5, 31)
    result = dcfc_30_360_isda(start=ex4_start, asof=ex4_asof, end=ex4_asof)
    assert round(result, 14) == Decimal('1.33333333333333')
