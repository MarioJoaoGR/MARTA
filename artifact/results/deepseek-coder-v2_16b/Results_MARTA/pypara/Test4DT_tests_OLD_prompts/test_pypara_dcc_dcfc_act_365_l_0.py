
import pytest
from datetime import date, timedelta
from decimal import Decimal
from unittest.mock import patch
from pypara.dcc import dcfc_act_365_l



def test_error_case_invalid_dates():
    with pytest.raises(ValueError):
        start = date(2023, 13, 1)  # Invalid month