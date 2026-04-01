
import pytest
from typing import Optional, List, Any
from dataclasses_json.utils import _is_optional, _issubclass_safe, _hasargs

def test_valid_case_1():
    assert _is_optional(Optional[int]) == True
    assert _is_optional(List[int]) == False
    assert _is_optional(Any) == True
