
import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_act_365_a

def _has_leap_day(start, end):
    # Helper function to determine if there is a leap day in the period
    return start <= date(start.year, 2, 29) and (end >= date(end.year, 3, 1) or end == date(end.year, 2, 29))

def _get_actual_day_count(start, end):
    # Helper function to calculate the actual number of days between two dates
    return (end - start).days + 1 if start <= end else (start - end).days + 1

@pytest.mark.parametrize("start, asof, end, expected", [
    (date(2007, 12, 28), date(2008, 2, 28), date(2008, 2, 28), Decimal('0.16986301369863')),
    (date(2007, 12, 28), date(2008, 2, 29), date(2008, 2, 29), Decimal('0.17213114754098')),
    (date(2007, 10, 31), date(2008, 11, 30), date(2008, 11, 30), Decimal('1.08196721311475')),
    (date(2008, 2, 1), date(2009, 5, 31), date(2009, 5, 31), Decimal('1.32513661202186'))
])
def test_dcfc_act_365_a(start, asof, end, expected):
    result = dcfc_act_365_a(start=start, asof=asof, end=end)
    assert round(result, 14) == expected
