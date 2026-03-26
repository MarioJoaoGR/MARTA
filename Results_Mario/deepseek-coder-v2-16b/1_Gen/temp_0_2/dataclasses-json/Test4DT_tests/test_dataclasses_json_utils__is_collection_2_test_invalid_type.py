
import pytest
from dataclasses_json.utils import _is_collection, _get_type_origin
from collections.abc import Collection

def test_invalid_type():
    class MyCustomType: pass
    
    # Test with an invalid or unsupported type that should return False
    assert not _is_collection(MyCustomType)
