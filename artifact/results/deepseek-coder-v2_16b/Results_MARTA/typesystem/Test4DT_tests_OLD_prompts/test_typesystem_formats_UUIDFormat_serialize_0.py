
import pytest
from typesystem.formats import UUIDFormat
import uuid

# Test for validating a valid UUID

# Test for validating an invalid UUID

# Test for serializing a valid UUID
def test_serialize_valid_UUID():
    uuid_format = UUIDFormat()
    result = uuid_format.serialize("123e4567-e89b-12d3-a456-426614174000")
    assert result == "123e4567-e89b-12d3-a456-426614174000"

# Test for serializing an invalid UUID