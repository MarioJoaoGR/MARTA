
import pytest
from datetime import datetime
from typesystem.formats import DateTimeFormat

# Initialize the DateTimeFormat class for testing
@pytest.fixture
def dt_format():
    return DateTimeFormat()

# Test cases for is_native_type method
def test_is_native_type_valid_datetime(dt_format):
    # Arrange
    value = datetime(2023, 4, 1, 12, 0, 0)
    
    # Act
    result = dt_format.is_native_type(value)
    
    # Assert
    assert result is True, "Expected is_native_type to return True for a valid datetime object"

def test_is_native_type_invalid_type(dt_format):
    # Arrange
    value = "2023-04-01 12:00:00"
    
    # Act
    result = dt_format.is_native_type(value)
    
    # Assert
    assert result is False, "Expected is_native_type to return False for a string that is not a datetime object"

def test_is_native_type_none(dt_format):
    # Arrange
    value = None
    
    # Act
    result = dt_format.is_native_type(value)
    
    # Assert
    assert result is False, "Expected is_native_type to return False for a None value"

def test_is_native_type_int(dt_format):
    # Arrange
    value = 12345
    
    # Act
    result = dt_format.is_native_type(value)
    
    # Assert
    assert result is False, "Expected is_native_type to return False for an integer"
