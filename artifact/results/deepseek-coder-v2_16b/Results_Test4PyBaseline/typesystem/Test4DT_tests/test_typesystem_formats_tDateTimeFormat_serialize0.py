
# Module: typesystem.formats
import pytest
from datetime import datetime, timezone, timedelta
from typesystem.formats import DateTimeFormat

# Fixture to create an instance of DateTimeFormat for each test
@pytest.fixture
def formatter():
    return DateTimeFormat()

# Test case for serializing a valid datetime object
def test_serialize_valid_datetime(formatter):
    dt = datetime(2023, 4, 1, 12, 0, 0)
    result = formatter.serialize(dt)
    assert isinstance(result, str), "Expected serialized datetime to be a string"