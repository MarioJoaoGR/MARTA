
import pytest
from datetime import timedelta as td
import pysnooper.pycompat  # Assuming the module name is correct and contains the function

# Test case for parsing a time duration string with hours, minutes, seconds, and microseconds
def test_timedelta_parse_with_all_components():
    s = '1:20:30.123456'
    result = pysnooper.pycompat.timedelta_parse(s)
    expected = td(days=0, seconds=4830, microseconds=123456)
    assert result == expected

# Test case for parsing a time duration string with zero values for hours, minutes, and microseconds
def test_timedelta_parse_with_zero_components():
    s = '0:0:0.999999'
    result = pysnooper.pycompat.timedelta_parse(s)
    expected = td(days=0, seconds=0, microseconds=999999)