
import pytest
from pypara.dcc import dcfc_act_act_icma
import datetime
from decimal import Decimal

# Helper function to get actual day count for testing purposes
def _get_actual_day_count(start, end):
    # This is a placeholder implementation for the sake of example
    return (end - start).days

# Test cases for valid inputs
@pytest.mark.parametrize("start_date, asof_date, end_date", [
    (datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2))
])
def test_valid_case(start_date, asof_date, end_date):
    result = dcfc_act_act_icma(start=start_date, asof=asof_date, end=end_date, freq=Decimal('1'))
    assert isinstance(result, Decimal), "Result should be a Decimal"
    # Add more specific assertions if needed based on expected behavior

# Test cases for edge inputs (None values)
@pytest.mark.parametrize("start_date, asof_date, end_date", [
    (None, None, None)
])
def test_edge_case(start_date, asof_date, end_date):
    with pytest.raises(TypeError):
        dcfc_act_act_icma(start=start_date, asof=asof_date, end=end_date)

# Test cases for error inputs (string values instead of datetime objects)
@pytest.mark.parametrize("start_date, asof_date, end_date", [
    ('2019-3-2', '2019-9-10', '2020-3-2')
])
def test_error_case(start_date, asof_date, end_date):
    with pytest.raises(TypeError):
        dcfc_act_act_icma(start=start_date, asof=asof_date, end=end_date)
