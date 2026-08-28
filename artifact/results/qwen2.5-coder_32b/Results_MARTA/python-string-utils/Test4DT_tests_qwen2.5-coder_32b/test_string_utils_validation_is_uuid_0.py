
import pytest
from uuid import UUID
from string_utils.validation import is_uuid

# Test standard UUID format
def test_valid_uuid_standard_format():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True

# Test hexadecimal UUID format with allow_hex=True
def test_valid_uuid_hex_format_allowed():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', True) == True

# Test invalid UUID format
def test_invalid_uuid_standard_format():
    assert is_uuid('invalid-uuid-string') == False

# Test hexadecimal UUID format with allow_hex=False (default)
def test_invalid_uuid_hex_format_not_allowed():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf') == False

# Test UUID object in standard format
def test_valid_uuid_object_standard_format():
    valid_uuid_obj = UUID('6f8aa2f9-686c-4ac3-8766-5712354a04cf')
    assert is_uuid(valid_uuid_obj) == True

# Test UUID object in hexadecimal format with allow_hex=True
def test_valid_uuid_object_hex_format_allowed():
    hex_uuid_obj = UUID('6f8aa2f9-686c-4ac3-8766-5712354a04cf')
    assert is_uuid(hex_uuid_obj.hex, True) == True

# Test None input
def test_none_input():
    assert is_uuid(None) == False

# Test empty string input
def test_empty_string():
    assert is_uuid('') == False
