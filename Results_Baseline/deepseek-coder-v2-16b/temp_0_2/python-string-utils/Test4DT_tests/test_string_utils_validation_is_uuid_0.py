# Module: string_utils.validation
import pytest
from string_utils.validation import is_uuid

# Test cases for valid UUIDs
def test_valid_standard_uuid():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True

def test_valid_hex_uuid():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) == True

# Test cases for invalid UUIDs
def test_invalid_standard_uuid():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cg') == False

def test_invalid_hex_uuid():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cg', allow_hex=True) == False

# Test cases for non-UUID strings
def test_non_uuid_string():
    assert is_uuid('not a uuid') == False

def test_empty_string():
    assert is_uuid('') == False

# Test cases for valid UUIDs with different formats (though the function only checks standard or hex format)
def test_valid_standard_uuid_different_format():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True

# Test cases for invalid UUIDs with different formats (though the function only checks standard or hex format)
def test_invalid_standard_uuid_different_format():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cg') == False

# Test cases for valid UUIDs with different casing (though the function only checks standard or hex format)
def test_valid_standard_uuid_different_case():
    assert is_uuid('6f8aa2F9-686c-4ac3-8766-5712354a04cf') == True  # Case insensitive check (UUID format itself does not care about case)
