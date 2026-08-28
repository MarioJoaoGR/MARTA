
import pytest
import uuid
from typesystem.formats import UUIDFormat

# Create an instance of UUIDFormat
uuid_format = UUIDFormat()

def test_validate_valid_uuid():
    valid_uuid = "123e4567-e89b-12d3-a456-426614174000"
    result = uuid_format.validate(valid_uuid)
    assert isinstance(result, uuid.UUID), f"Expected a UUID object but got {type(result)}"