
import pytest
from dataclasses_json import utils  # Assuming this is the correct module path
from typing import Optional, List, Any

# Mocking the necessary functions since they are not defined in the provided code snippet
def _issubclass_safe(cls, base):
    return issubclass(cls, base)

def _hasargs(cls, arg_type):
    return any(arg == arg_type for arg in cls.__args__)

# Assuming utils module has the function _is_optional defined as per the docstring
def test_valid_case_2():
    assert utils._is_optional(Optional[int]) is True
    assert utils._is_optional(List[int]) is False
    assert utils._is_optional(Any) is True
