
import pytest
from datetime import timedelta as td
import pysnooper.pycompat as pycompat

def test_valid_input():
    result = pycompat.timedelta_parse('1:20:30.123456')
    assert isinstance(result, td)
    assert result == td(days=0, seconds=4830, microseconds=123456)

def test_zero_values():
    result = pycompat.timedelta_parse('0:0:0.999999')
    assert isinstance(result, td)
    assert result == td(days=0, seconds=0, microseconds=999999)

def test_invalid_input():
    with pytest.raises(ValueError):
        pycompat.timedelta_parse('invalid input')
