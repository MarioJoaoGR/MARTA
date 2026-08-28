
import pytest
from unittest.mock import MagicMock, patch
from typesystem.base import ValidationError

class MySchema:
    @staticmethod
    def validate_or_error(data):
        if data == "invalid data":
            return (None, ValidationError('Validation failed'))
        else:
            return (data, None)

def test_valid_input():
    with patch('typesystem.base.ValidationError', MagicMock()):
        result = MySchema.validate_or_error({"key": "value"})
        assert isinstance(result[0], dict), "Expected validated data to be a dictionary"
        assert result[1] is None, "Expected no error for valid input"

