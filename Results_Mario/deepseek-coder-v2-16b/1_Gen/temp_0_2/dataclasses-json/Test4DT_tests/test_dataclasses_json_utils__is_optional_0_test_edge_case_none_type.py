
import pytest
from dataclasses_json.utils import _is_optional
from typing import Optional, List, Union, Any

def test_edge_case_none_type():
    # Test when type is None directly
    assert not _is_optional(None)
    
    # Test when type is a regular non-Optional type
    class MyType: pass
    assert not _is_optional(MyType)
    
    # Test when type is Optional[int]
    assert _is_optional(Optional[int])
    
    # Test when type is Union[int, None] (which should be treated as optional by the function)
    assert _is_optional(Union[int, None])
    
    # Additional tests can go here to cover different scenarios and edge cases
