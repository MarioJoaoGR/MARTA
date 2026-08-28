
# Module: typesystem.formats
import pytest
from typesystem.formats import BaseFormat
from datetime import date
import typing  # Importing typing module for type hints

# Assuming there is a ValidationError class in the module 'typesystem' with a text attribute for error messages
class ValidationError(Exception):
    def __init__(self, message):
        self.text = message

# Mocking the DateFormat class to simulate the functionality of the BaseFormat class
class DateFormat(BaseFormat):
    def validate(self, value: typing.Any) -> typing.Union[date, ValidationError]:
        try:
            parsed_date = date.fromisoformat(value)
            return parsed_date
        except ValueError:
            raise ValidationError("Must be a valid date format.")

    def serialize(self, value: date) -> str:
        return value.strftime("%Y-%m-%d")

# Test cases for the DateFormat class
def test_validate_valid_date():
    df = DateFormat()
    validated_date = df.validate("2023-10-31")
    assert isinstance(validated_date, date), "Expected a datetime.date object"

def test_validate_invalid_date():
    df = DateFormat()
    with pytest.raises(ValidationError) as e:
        df.validate("invalid-date")
    assert str(e.value) == "Must be a valid date format.", "Expected error message about invalid date format"

def test_serialize_native_date():
    df = DateFormat()
    today = date.today()
    serialized_date = df.serialize(today)
    assert isinstance(serialized_date, str), "Expected a string representation of the date"
    assert serialized_date == today.strftime("%Y-%m-%d"), "Serialized date format is incorrect"
