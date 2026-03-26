
import pytest
from collections import defaultdict
from typing import Mapping

def _get_type_origin(type_):
    if hasattr(type_, '__origin__'):
        return type_.__origin__
    return type_

def _issubclass_safe(cls, class_or_tuple):
    try:
        return issubclass(cls, class_or_tuple)
    except TypeError:
        return False

def _is_mapping(type_):
    return _issubclass_safe(_get_type_origin(type_), Mapping)

@pytest.mark.parametrize("invalid_input", [None, [], set(), "string", 123])
def test_invalid_input(invalid_input):
    assert not _is_mapping(invalid_input), f"Expected _is_mapping({invalid_input}) to be False, but got True"
