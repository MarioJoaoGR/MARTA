
import uuid as stdlib_uuid
from string_utils.generation import uuid
import pytest

def test_valid_uuid_default():
    # Test default UUID generation
    uid = uuid()
    assert isinstance(uid, str), "Expected a string"
    parsed_uuid = stdlib_uuid.UUID(uid)
    assert parsed_uuid is not None, "Failed to parse the generated UUID"

    # Test hexadecimal representation of UUID
    hex_uid = uuid(as_hex=True)
    assert isinstance(hex_uid, str), "Expected a string"
    parsed_hex_uuid = stdlib_uuid.UUID(hex_uid)
    assert parsed_hex_uuid is not None, "Failed to parse the generated hexadecimal UUID"
