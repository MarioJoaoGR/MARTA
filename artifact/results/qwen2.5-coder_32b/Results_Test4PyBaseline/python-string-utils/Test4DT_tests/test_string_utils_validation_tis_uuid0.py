# Module: string_utils.validation
import pytest
from uuid import UUID
from string_utils.validation import is_uuid

# Regular test cases for standard UUID format
def test_is_uuid_standard_format():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True
    assert is_uuid('123e4567-e89b-12d3-a456-426614174000') == True

# Test cases for invalid UUID format
def test_is_uuid_invalid_format():
    assert is_uuid('invalid-uuid-string') == False
    assert is_uuid('123e4567-e89b-12d3-a456-42661417400') == False  # Missing one character
    assert is_uuid('123e4567-e89b-12d3-a456-4266141740000') == False  # Extra character

# Test cases for hexadecimal UUID format without allow_hex=True
def test_is_uuid_hex_format_disallowed():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf') == False
    assert is_uuid('123e4567e89b12d3a456426614174000') == False

# Test cases for hexadecimal UUID format with allow_hex=True
def test_is_uuid_hex_format_allowed():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) == True
    assert is_uuid('123e4567e89b12d3a456426614174000', allow_hex=True) == True

# Test cases for UUID object input
def test_is_uuid_with_uuid_object():
    valid_uuid = UUID('6f8aa2f9-686c-4ac3-8766-5712354a04cf')
    assert is_uuid(valid_uuid) == True

# Edge cases with different types of input
def test_is_uuid_with_non_string_input():
    assert is_uuid(12345678901234567890123456789012) == False  # Integer
    assert is_uuid(None) == False  # NoneType
    assert is_uuid([]) == False  # List
    assert is_uuid({}) == False  # Dictionary

# Test cases with empty string and whitespace
def test_is_uuid_with_empty_and_whitespace():
    assert is_uuid('') == False
    assert is_uuid('   ') == False
