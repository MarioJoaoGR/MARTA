
import pytest
from dataclasses_json.utils import _get_type_origin, _issubclass_safe
from collections import Counter

# Mocking the functions since they are not defined in the provided module
def mock__get_type_origin(type_):
    return type_ if isinstance(type_, type) else type_.__origin__

def mock__issubclass_safe(cls, subclass):
    return issubclass(cls, subclass)

# Monkey patching the functions for the test
@pytest.fixture(autouse=True)
def patch_functions():
    _get_type_origin = mock__get_type_origin
    _issubclass_safe = mock__issubclass_safe

# Test case to check if a given type is a subclass of Counter
@pytest.mark.parametrize("type_, expected", [
    (list, False),  # list is not a subclass of Counter
    (Counter, True),  # Counter itself is a subclass of Counter
    (list[int], False),  # list[int] is not a subclass of Counter
    (Counter[int], True)  # Counter[int] is a subclass of Counter
])
def test_valid_case_subclass(type_, expected):
    from dataclasses_json.utils import _is_counter
    
    assert _is_counter(type_) == expected
