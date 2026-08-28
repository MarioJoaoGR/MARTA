
import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_30_360_german

def _is_last_day_of_month(date):
    # Helper function to check if a given date is the last day of a month
    next_month = date.replace(day=28) + datetime.timedelta(days=4)
    return next_month.month != date.month

@pytest.mark.parametrize("start, asof, end, expected", [
    (date(2007, 12, 28), date(2008, 2, 28), date(2008, 2, 28), Decimal('0.16666666666667')),
    (date(2007, 12, 28), date(2008, 2, 29), date(2008, 2, 29), Decimal('0.16944444444444')),
    (date(2007, 10, 31), date(2008, 11, 30), date(2008, 11, 30), Decimal('1.08333333333333')),
    (date(2008, 2, 1), date(2009, 5, 31), date(2009, 5, 31), Decimal('1.33055555555556'))
])
def test_dcfc_30_360_german(start, asof, end, expected):
    result = dcfc_30_360_german(start=start, asof=asof, end=end)
    assert round(result, 14) == expected
