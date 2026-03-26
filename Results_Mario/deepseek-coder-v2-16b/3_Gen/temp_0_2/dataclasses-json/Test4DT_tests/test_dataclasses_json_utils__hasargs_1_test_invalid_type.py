
import pytest
from dataclasses_json.utils import _hasargs

def test_invalid_type():
    class MyType:
        __args__ = None  # This makes it a valid type with no arguments
    
    assert not _hasargs(MyType, 'a')  # Should return False since 'a' is not in an empty tuple of args
