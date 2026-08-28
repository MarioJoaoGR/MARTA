
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError, is_string
from uuid import UUID

def test___StringFormatter___placeholder_key_basic():
    formatter = __StringFormatter("Sample text")
    placeholder_key = formatter._StringFormatter__placeholder_key()
    
    # Ensure the placeholder key starts and ends with '$'
    assert placeholder_key.startswith('$') and placeholder_key.endswith('$')
    
    # Ensure the content between '$' is a valid UUID
    uuid_part = placeholder_key[1:-1]
    assert UUID(uuid_part)
