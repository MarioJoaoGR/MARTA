
import json
from string_utils.validation import is_json

def test_is_json_basic():
    # Test with a valid JSON object
    assert is_json('{"name": "Peter"}') == True
    
    # Test with a valid JSON array
    assert is_json('[1, 2, 3]') == True
    
    # Test with an invalid JSON string
    assert is_json('{nope}') == False
    
    # Test with an empty string
    assert is_json('') == False
    
    # Test with a string containing only spaces
    assert is_json('   ') == False
    
    # Test with a valid nested JSON object
    assert is_json('{"key": "value", "another_key": [1, 2, {"nested": true}]}') == True
    
    # Test with a number (not a valid JSON)
    assert is_json('42') == False
