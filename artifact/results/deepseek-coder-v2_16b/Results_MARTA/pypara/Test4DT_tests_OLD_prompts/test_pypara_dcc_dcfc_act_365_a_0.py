
import pytest
from datetime import date, timedelta
from decimal import Decimal
from unittest.mock import patch
from pypara.dcc import dcfc_act_365_a

def _has_leap_day(start, end):
    return start <= date(start.year, 2, 29) and end >= date(end.year, 2, 29)

def _get_actual_day_count(start, end):
    delta = end - start
    return Decimal(delta.days)

@pytest.mark.parametrize("start_date, asof_date, end_date, expected", [
    (date(2007, 12, 28), date(2008, 2, 28), date(2008, 2, 28), Decimal('0.16986301369863')),
    (date(2007, 12, 28), date(2008, 2, 29), date(2008, 2, 29), Decimal('0.17213114754098')),
    (date(2007, 10, 31), date(2008, 11, 30), date(2008, 11, 30), Decimal('1.08196721311475')),
    (date(2008, 2, 1), date(2009, 5, 31), date(2009, 5, 31), Decimal('1.32513661202186'))
])
def test_dcfc_act_365_a(start_date, asof_date, end_date, expected):
    with patch('pypara.dcc._get_actual_day_count', return_value=_get_actual_day_count(start_date, end_date)):
        result = dcfc_act_365_a(start=start_date, asof=asof_date, end=end_date)
        assert round(result, 14) == expected
