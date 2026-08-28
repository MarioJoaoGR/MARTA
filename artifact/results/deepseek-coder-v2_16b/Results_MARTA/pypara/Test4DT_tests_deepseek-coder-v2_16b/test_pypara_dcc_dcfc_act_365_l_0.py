
import pytest
from datetime import date
from decimal import Decimal
import calendar
from pypara.dcc import dcfc_act_365_l

def _get_actual_day_count(start, end):
    # Helper function to calculate the actual number of days between two dates
    return (end - start).days

@pytest.mark.parametrize("start, asof, end, expected", [
    (date(2023, 1, 1), date(2023, 7, 1), date(2023, 12, 31), Decimal('0.49589041095890')),
    (date(2024, 1, 1), date(2024, 7, 1), date(2025, 6, 30), Decimal('0.49726775956284'))
])
def test_dcfc_act_365_l(start, asof, end, expected):
    result = dcfc_act_365_l(start=start, asof=asof, end=end)
    assert round(result, 14) == expected

@pytest.mark.parametrize("start, asof, end, freq, expected", [
    (date(2023, 1, 1), date(2023, 7, 1), date(2023, 12, 31), Decimal('2'), Decimal('0.49589041095890'))
])
def test_dcfc_act_365_l_optional_frequency(start, asof, end, freq, expected):
    result = dcfc_act_365_l(start=start, asof=asof, end=end, freq=freq)
    assert round(result, 14) == expected
