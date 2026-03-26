
import pytest
from dataclasses_json.core import _encode_json_type
from typing import List, Dict, Union

def test_invalid_input():
    # Test with a non-list and non-dict input
    assert _encode_json_type("not a list or dict") == "not a list or dict"
    
    # Test with an integer (which is not a list or dict)
    assert _encode_json_type(12345) == 12345
    
    # Test with a float (which is not a list or dict)
    assert _encode_json_type(123.45) == 123.45
    
    # Test with a string (which is not a list or dict)
    assert _encode_json_type("string") == "string"
    
    # Test with None (which is not a list or dict)
    assert _encode_json_type(None) is None
