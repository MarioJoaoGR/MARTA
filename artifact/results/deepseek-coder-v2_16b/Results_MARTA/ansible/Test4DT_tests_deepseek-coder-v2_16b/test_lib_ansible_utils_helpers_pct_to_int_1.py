
import pytest
from ansible.utils.helpers import pct_to_int


def test_valid_case_percentage_input():
    value = "30%"
    num_items = 300
    result = pct_to_int(value, num_items)
    assert result == int((float(value.strip('%')) / 100.0) * num_items)

def test_case_with_min_value():
    value = 15
    num_items = 100
    min_value = 5
    result = pct_to_int(value, num_items, min_value)
    assert result == max(int((value / 100.0) * num_items), min_value)