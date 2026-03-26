
import pytest
from dataclasses_json.utils import _hasargs

def test_none_input():
    class MyType:
        __args__ = None
    
    assert not _hasargs(MyType, 'a')  # True if all specified arguments are in the type's __args__, False otherwise.
