
import pytest
from string_utils.validation import is_json

def test_valid_json_string():
    # Test a valid JSON string
    assert is_json('{"name": "Peter"}') == True
    
    # Test a valid JSON array string
    assert is_json('[1, 2, 3]') == True
    
    # Test an invalid JSON string
    assert is_json('{nope}') == False
