
import pytest
from typesystem.formats import UUIDFormat
import uuid

# Scenario 1: Test valid UUID input

# Scenario 2: Test invalid UUID input (should return False)
def test_invalid_uuid():
    uuid_format = UUIDFormat()
    some_value = '123e4567-e89b-12d3-a456-42661417400'  # Missing trailing character
    assert not uuid_format.is_native_type(some_value)

# Scenario 3: Test None input (should raise TypeError)