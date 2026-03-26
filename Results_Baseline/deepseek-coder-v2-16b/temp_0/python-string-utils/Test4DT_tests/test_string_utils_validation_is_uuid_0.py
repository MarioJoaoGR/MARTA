
import pytest
from string_utils.validation import is_uuid
from uuid import UUID

# Test cases for valid UUIDs with default settings
def test_valid_standard_uuid():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True

# Test cases for valid UUIDs with allow_hex=True
def test_valid_hex_uuid():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) == True

# Test cases for invalid UUIDs with default settings
def test_invalid_standard_uuid():
    assert is_uuid('not-a-valid-uuid') == False

# Test cases for invalid UUIDs with allow_hex=True (should be treated as valid hex string)
def test_invalid_hex_uuid():
    assert not is_uuid('not-a-valid-hex', allow_hex=True) == True

# Edge case: empty string should not be a valid UUID
def test_empty_string_is_not_uuid():
    assert not is_uuid('')

# Edge case: None should not be a valid UUID
def test_none_is_not_uuid():
    assert not is_uuid(None)

# Edge case: short string without hyphens should not be a valid UUID
def test_short_string_without_hyphens_is_not_uuid():
    assert not is_uuid('6f8aa2f9686c4ac387665712354a04cf')
