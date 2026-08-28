
# Module: string_utils.validation
import pytest
from string_utils.validation import is_uuid
from uuid import UUID
import re  # Importing the 're' module here as it was not recognized previously

# Define the regex patterns for UUID and hex-encoded UUID as per the function implementation
UUID_RE = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.IGNORECASE)
UUID_HEX_OK_RE = re.compile(r'^[0-9a-f]{32}$', re.IGNORECASE)

# Test cases for standard UUIDs
def test_is_uuid_standard():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cg') == False  # Invalid UUID

# Test cases for hex-encoded UUIDs with allow_hex=True
def test_is_uuid_hex_allow():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) == True
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cg', allow_hex=True) == False  # Invalid hex UUID

# Test cases for standard UUIDs with default setting (allow_hex=False)
def test_is_uuid_standard_default():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cg') == False

# Test cases for hex-encoded UUIDs with default setting (allow_hex=False)
def test_is_uuid_hex_default():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf') == False

# Additional edge cases to consider
def test_is_uuid_edge_cases():
    # Empty string should not be a valid UUID
    assert is_uuid('') == False
    # Non-string input should not be considered a valid UUID
    assert is_uuid(None) == False
    # Short hex strings should not be considered valid UUIDs even with allow_hex=True
    assert is_uuid('123456789abcdef') == False  # Hex string too short to be a UUID

# Test cases for function documentation examples
def test_is_uuid_examples():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True  # Standard UUID example
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) == True  # Hex-encoded UUID example
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cg') == False  # Invalid standard UUID example
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf') == False  # Hex-encoded but default setting does not allow hex
