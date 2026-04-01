
import pytest
from typing import Optional, List, Any
from dataclasses_json.utils import _is_optional  # Assuming this is the correct import path

def test_invalid_input():
    """Test that invalid inputs return False."""
    
    # Test with an invalid type (not a class or type object)
    assert not _is_optional(42), "Expected False for non-type input"
    
    # Test with a valid but unsupported type
    class MyType: pass
    assert not _is_optional(MyType), "Expected False for unsupported types"
    
    # Test with a list, which is not an Optional type
    assert not _is_optional(List[int]), "Expected False for List type"
