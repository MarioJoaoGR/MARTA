
import re
from unittest.mock import patch
from string_utils.validation import is_uuid  # Assuming this module contains the `is_uuid` function

# Define regular expressions for UUID validation
UUID_RE = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.IGNORECASE)
UUID_HEX_OK_RE = re.compile(r'^[0-9a-f]{32}$', re.IGNORECASE)

def test_is_uuid():
    # Test a valid UUID string
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True
    
    # Test a non-UUID hex string without allow_hex
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf') == False
    
    # Test a valid UUID hex string with allow_hex
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) == True
