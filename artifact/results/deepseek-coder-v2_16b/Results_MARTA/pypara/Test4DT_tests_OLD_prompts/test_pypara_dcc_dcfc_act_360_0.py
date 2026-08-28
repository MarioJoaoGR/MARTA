
import pytest
from datetime import date
from decimal import Decimal
from unittest.mock import patch
from pypara.dcc import dcfc_act_360, _get_actual_day_count



@patch('pypara.dcc._get_actual_day_count', return_value=Decimal(365))
def test_invalid_dates(mock_get_actual_day_count):
    start = date(2020, 12, 31)
    end = date(2020, 1, 1)
    with pytest.raises(TypeError):
        dcfc_act_360(start=start, end=end)