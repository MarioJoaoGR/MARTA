
import pytest
from typesystem.formats import DateFormat
from datetime import date

def test_serialize_valid_date():
    df = DateFormat()
    valid_date = date(2023, 10, 5)
    result = df.serialize(valid_date)
    assert result == '2023-10-05'

def test_serialize_none():
    df = DateFormat()
    result = df.serialize(None)
    assert result is None

def test_serialize_invalid_type():
    df = DateFormat()
    with pytest.raises(AssertionError):
        df.serialize("not a date")
