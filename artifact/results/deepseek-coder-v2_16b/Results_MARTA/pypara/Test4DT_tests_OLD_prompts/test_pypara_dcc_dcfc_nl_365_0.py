
import pytest
from datetime import date, timedelta
from decimal import Decimal
from unittest.mock import patch
from pypara.dcc import _get_actual_day_count, _has_leap_day, dcfc_nl_365

@pytest.mark.parametrize("start, asof, end, expected", [
    (date(2007, 12, 28), date(2008, 2, 28), date(2008, 2, 28), Decimal('0.16986301369863')),
    (date(2007, 12, 28), date(2008, 2, 29), date(2008, 2, 29), Decimal('0.16986301369863')),
    (date(2007, 10, 31), date(2008, 11, 30), date(2008, 11, 30), Decimal('1.08219178082192')),
    (date(2008, 2, 1), date(2009, 5, 31), date(2009, 5, 31), Decimal('1.32602739726027'))
])
def test_dcfc_nl_365(start, asof, end, expected):
    with patch('pypara.dcc._get_actual_day_count', side_effect=_get_actual_day_count), \
         patch('pypara.dcc._has_leap_day', side_effect=_has_leap_day):
        result = dcfc_nl_365(start=start, asof=asof, end=end)
        assert round(result, 14) == expected
