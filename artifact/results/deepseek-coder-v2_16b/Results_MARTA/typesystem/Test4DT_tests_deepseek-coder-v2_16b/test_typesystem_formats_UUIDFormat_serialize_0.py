
import pytest
from typesystem.formats import UUIDFormat

# Scenario 1: Test serialization of a valid UUID
def test_valid_uuid_serialization():
    uuid_format = UUIDFormat()
    valid_uuid = "123e4567-e89b-12d3-a456-426614174000"
    result = uuid_format.serialize(valid_uuid)
    assert isinstance(result, str), f"Expected a string representation of UUID but got {type(result)}"
    assert result == valid_uuid, f"Expected '{valid_uuid}' but got '{result}'"

# Scenario 2: Test serialization of an invalid UUID, should raise ValueError

# Scenario 3: Test serialization of None, should raise TypeError or ValueError depending on implementation details