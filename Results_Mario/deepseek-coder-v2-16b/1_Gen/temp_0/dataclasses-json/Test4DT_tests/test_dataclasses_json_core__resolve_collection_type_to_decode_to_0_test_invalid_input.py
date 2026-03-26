
import pytest
from collections import deque
from dataclasses_json.core import _resolve_collection_type_to_decode_to, _get_type_cons

def test_invalid_input():
    # Test with an invalid type (e.g., a string) to ensure it defaults to the original type
    invalid_type = str
    resolved_type = _resolve_collection_type_to_decode_to(invalid_type)
    
    assert isinstance(resolved_type, type), "Expected the resolved type to be a class"
    assert resolved_type == invalid_type, f"Expected {invalid_type} but got {resolved_type}"
