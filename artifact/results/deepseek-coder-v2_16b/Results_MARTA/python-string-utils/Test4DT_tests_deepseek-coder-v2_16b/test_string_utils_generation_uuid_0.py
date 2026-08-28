
import pytest
from uuid import uuid4
from string_utils.generation import uuid

def test_uuid_default():
    result = uuid()
    assert isinstance(result, str), f"Expected a string, but got {type(result).__name__}"
    # Check if the default UUID is in standard format (36 characters)
    assert len(result.replace('-', '')) == 32, "Default UUID should be in standard format without hyphens."

def test_uuid_hex():
    result = uuid(as_hex=True)
    assert isinstance(result, str), f"Expected a string, but got {type(result).__name__}"
    # Check if the hex UUID is in hexadecimal format (32 characters without hyphens)
    assert len(result) == 32, "Hexadecimal UUID should be in standard format without hyphens."
    # Ensure all characters are valid hexadecimal digits
    assert all(c in '0123456789abcdef' for c in result), "All characters in the hex UUID should be hexadecimal digits."
