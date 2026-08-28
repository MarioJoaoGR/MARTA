
import pytest
from unittest.mock import patch
from typesystem.formats import DateFormat, ValidationError
import datetime

# Test valid date format input
def test_valid_date_format():
    with patch('typesystem.formats.DateFormat.validate', return_value=datetime.date(2023, 10, 15)):
        date_format = DateFormat()
        result = date_format.validate("2023-10-15")
        assert isinstance(result, datetime.date)

# Test invalid date format input
def test_invalid_date_format():
    with pytest.raises(ValidationError) as exc_info:
        date_format = DateFormat()
        date_format.validate("not-a-valid-format")
    assert str(exc_info.value) == "Must be a valid date format."

# Test invalid date value input
def test_invalid_date_value():
    with pytest.raises(ValidationError) as exc_info:
        date_format = DateFormat()
        date_format.validate("2023-10-99")  # Invalid day
    assert str(exc_info.value) == "Must be a real date."
