
import pytest
from datetime import datetime
from typesystem.formats import DateTimeFormat

# Test for valid datetime input
def test_valid_datetime_input():
    dt_format = DateTimeFormat()
    now = datetime.now()
    result = dt_format.serialize(now)
    assert isinstance(result, str), "Expected a string representation of the datetime"
    assert len(result) > 0, "Expected a non-empty string"

# Test for handling None input
def test_none_input():
    dt_format = DateTimeFormat()
    result = dt_format.serialize(None)
    assert result is None, "Expected None when input is None"

# Test for raising AssertionError with an invalid type input
def test_invalid_type_input():
    dt_format = DateTimeFormat()
    with pytest.raises(AssertionError):
        dt_format.serialize("not a datetime")
