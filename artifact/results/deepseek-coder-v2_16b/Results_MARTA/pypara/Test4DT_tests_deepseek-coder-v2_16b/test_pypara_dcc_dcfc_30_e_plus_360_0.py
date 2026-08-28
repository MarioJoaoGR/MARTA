
import pytest
from datetime import date, timedelta
from decimal import Decimal
from pypara.dcc import dcfc_30_e_plus_360

def test_valid_dates():
    ex1_start = date(2007, 12, 28)
    ex1_asof = date(2008, 2, 28)
    assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

    ex2_start = date(2007, 12, 28)
    ex2_asof = date(2008, 2, 29)
    assert round(dcfc_30_e_plus_360(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16944444444444')

    ex3_start = date(2007, 10, 31)
    ex3_asof = date(2008, 11, 30)
    assert round(dcfc_30_e_plus_360(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08333333333333')

    ex4_start = date(2008, 2, 1)
    ex4_asof = date(2009, 5, 31)
    assert round(dcfc_30_e_plus_360(start=ex4_start, asof=ex4_asof, end=ex4_asof), 14) == Decimal('1.33333333333333')

