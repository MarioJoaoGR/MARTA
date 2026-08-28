
import pytest
from datetime import date, timedelta
from unittest.mock import patch
from pypara.dcc import _get_actual_day_count

@pytest.fixture(params=[
    (date(2023, 1, 1), date(2023, 1, 5)),
    (date(2023, 1, 1), date(2023, 1, 1))
])
def mock_dates(request):
    return request.param

def test_valid_input(mock_dates):
    mock_start, mock_end = mock_dates
    with patch('datetime.date', autospec=True) as mock_date:
        mock_date.return_value = mock_start
        assert _get_actual_day_count(mock_start, mock_end) == (mock_end - mock_start).days

def test_edge_case_same_date(mock_dates):
    mock_start, _ = mock_dates
    with patch('datetime.date', autospec=True) as mock_date:
        mock_date.return_value = mock_start
        assert _get_actual_day_count(mock_start, mock_start) == 0
