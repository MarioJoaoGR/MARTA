
import pytest
from string_utils.generation import uuid

def test_uuid_default_format():
    """Test that the default UUID format is correct."""
    generated_uuid = uuid()
    assert len(generated_uuid) == 36, "UUID should be 36 characters long"
    assert '-' in generated_uuid, "Default UUID should contain hyphens"

def test_uuid_hex_format():
    """Test that the hexadecimal UUID format is correct."""
    generated_uuid = uuid(as_hex=True)
    assert len(generated_uuid) == 32, "Hexadecimal UUID should be 32 characters long"
    assert '-' not in generated_uuid, "Hexadecimal UUID should not contain hyphens"


def test_valid_boolean_true():
    """Test that passing True for as_hex returns a valid hexadecimal UUID."""
    generated_uuid = uuid(as_hex=True)
    assert isinstance(generated_uuid, str), "UUID should be a string"
    assert len(generated_uuid) == 32, "Hexadecimal UUID should be 32 characters long"

def test_valid_boolean_false():
    """Test that passing False for as_hex returns a valid standard UUID."""
    generated_uuid = uuid(as_hex=False)
    assert isinstance(generated_uuid, str), "UUID should be a string"
    assert len(generated_uuid) == 36, "Standard UUID should be 36 characters long"

def test_default_value():
    """Test that the default value of as_hex is False."""
    generated_uuid = uuid()
    assert '-' in generated_uuid, "Default UUID should contain hyphens"