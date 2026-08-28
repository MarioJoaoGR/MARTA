
import pytest
from string_utils.validation import is_uuid

# Test valid UUID string with default settings
def test_valid_uuid_string():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True

# Test invalid UUID string without separators
def test_invalid_uuid_hex_without_allow_hex():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf') == False

# Test valid hex UUID with allow_hex=True
def test_valid_hex_uuid_with_allow_hex():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) == True
