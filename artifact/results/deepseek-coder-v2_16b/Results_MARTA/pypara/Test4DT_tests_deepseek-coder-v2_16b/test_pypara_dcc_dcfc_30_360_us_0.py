
import pytest
from datetime import date
from decimal import Decimal
from pypara.dcc import dcfc_30_360_us

def _is_last_day_of_month(date_obj):
    # Helper function to check if a date is the last day of a month
    return date_obj.replace(day=28) + (date_obj.day >= 29).replace(day=30) > date_obj

@pytest.mark.parametrize("start, asof, end, expected", [
    # Example 1: Basic usage with no frequency specified
    (date(2007, 12, 28), date(2008, 2, 28), date(2008, 2, 28), Decimal('0.16666666666667')),
    # Example 2: Usage with a specific frequency (optional parameter)
    (date(2007, 12, 28), date(2008, 2, 29), date(2008, 2, 29), Decimal('0.16944444444444')),
    # Example 3: Handling the last day of a month by specifying the 'asof' date
    (date(2007, 10, 31), date(2008, 11, 30), date(2008, 11, 30), Decimal('1.08333333333333')),
    # Example 4: Handling the last day of a month by specifying the 'asof' date with different dates
    (date(2008, 2, 1), date(2009, 5, 31), date(2009, 5, 31), Decimal('1.33333333333333'))
])
def test_dcfc_30_360_us(start, asof, end, expected):
    result = dcfc_30_360_us(start=start, asof=asof, end=end)
    assert round(result, 14) == expected
