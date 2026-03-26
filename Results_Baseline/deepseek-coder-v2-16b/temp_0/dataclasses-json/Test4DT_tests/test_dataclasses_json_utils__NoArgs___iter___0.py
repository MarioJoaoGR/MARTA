# Module: dataclasses_json.utils
import pytest
from dataclasses_json.utils import _NoArgs

# Test Case 1: Iterating over _NoArgs instance yields no arguments
def test_no_args_iterator():
    no_args = _NoArgs()
    iterator = iter(no_args)
    assert list(iterator) == []

# Test Case 2: Calling next on the iterator should raise StopIteration
def test_no_args_next():
    no_args = _NoArgs()
    iterator = iter(no_args)
    with pytest.raises(StopIteration):
        next(iterator)
