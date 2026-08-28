
import pytest
from string_utils.validation import is_uuid
import re

# Define a fixture for UUID regex pattern
@pytest.fixture(scope="module")
def uuid_regex():
    return re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', re.IGNORECASE)

# Define a fixture for hex UUID regex pattern
@pytest.fixture(scope="module")
def uuid_hex_regex():
    return re.compile(r'^[0-9a-f]{32}$', re.IGNORECASE)

# Test valid UUID string with default settings
def test_valid_uuid_string(uuid_regex):
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True
    assert uuid_regex.match('6f8aa2f9-686c-4ac3-8766-5712354a04cf') is not None

# Test invalid UUID string without separators
def test_invalid_uuid_string():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf') == False

# Test valid hex UUID with allow_hex=True
def test_valid_hex_uuid(uuid_hex_regex):
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) == True
    assert uuid_hex_regex.match('6f8aa2f9686c4ac387665712354a04cf') is not None
