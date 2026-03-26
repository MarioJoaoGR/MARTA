
import re
from typing import Any
from unittest.mock import patch
import string_utils.validation as validation

# Assuming UUID_RE and UUID_HEX_OK_RE are defined in string_utils.validation module
UUID_RE = re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')
UUID_HEX_OK_RE = re.compile(r'^[0-9a-fA-F]{32}$')

def test_valid_uuid():
    with patch.object(validation, 'UUID_RE', UUID_RE):
        with patch.object(validation, 'UUID_HEX_OK_RE', UUID_HEX_OK_RE):
            # Test valid standard UUID
            assert validation.is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') is True
            
            # Test invalid standard UUID (missing hyphen)
            assert validation.is_uuid('6f8aa2f9686c4ac387665712354a04cf') is False
            
            # Test valid hex UUID
            assert validation.is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) is True
            
            # Test invalid hex UUID (incorrect length)
            assert validation.is_uuid('6f8aa2f9686c4ac387665712354a04c') is False
