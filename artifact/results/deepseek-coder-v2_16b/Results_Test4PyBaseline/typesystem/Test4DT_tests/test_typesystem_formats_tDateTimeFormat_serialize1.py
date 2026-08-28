
# Module: typesystem.formats
import pytest
from datetime import datetime, timezone, timedelta
from typesystem.formats import DateTimeFormat

# Fixture to create an instance of DateTimeFormat for each test
@pytest.fixture
def formatter():
    return DateTimeFormat()

# Test case for handling None input
def test_serialize_none(formatter):
    result = formatter.serialize(None)
    assert result is None, "Expected serialize(None) to return None"

# Test case for serializing a valid datetime object with timezone adjustment
def test_serialize_valid_datetime_with_timezone_adjustment(formatter):
    dt = datetime(2023, 4, 1, 12, 0, 0, tzinfo=timezone.utc)
    result = formatter.serialize(dt)
    assert isinstance(result, str), "Expected serialized datetime to be a string"
    assert result == '2023-04-01T12:00:00Z', "Unexpected timezone adjustment in ISO format"
