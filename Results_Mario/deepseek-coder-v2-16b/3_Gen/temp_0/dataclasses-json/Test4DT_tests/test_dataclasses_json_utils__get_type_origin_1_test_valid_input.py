
import sys
from typing import List, Union
import pytest

# Assuming _NO_TYPE_ORIGIN is defined somewhere in your codebase
_NO_TYPE_ORIGIN = object()

def test_get_type_origin():
    from dataclasses_json.utils import _get_type_origin
    
    # Test List[int]
    my_list = List[int]
    assert _get_type_origin(my_list) == list
    
    # Test Union[int, str]
    mixed_types = Union[int, str]
    if sys.version_info.minor == 6:
        assert _get_type_origin(mixed_types) == type(None) or _get_type_origin(mixed_types) == mixed_types
    else:
        assert _get_type_origin(mixed_types) == Union
