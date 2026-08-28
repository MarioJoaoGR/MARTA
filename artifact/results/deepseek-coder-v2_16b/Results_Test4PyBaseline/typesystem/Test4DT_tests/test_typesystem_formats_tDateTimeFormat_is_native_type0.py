
import pytest
from datetime import datetime
from typesystem.formats import DateTimeFormat

# Initialize the DateTimeFormat class for testing
@pytest.fixture
def dt_format():
    return DateTimeFormat()

# Test cases for serialize method
def test_serialize_valid_datetime(dt_format):
    # Arrange
    dt = datetime(2023, 4, 1, 12, 0, 0)
    
    # Act
    result = dt_format.serialize(dt)
    
    # Assert
    assert isinstance(result, str), "Expected serialize to return a string for a valid datetime object"