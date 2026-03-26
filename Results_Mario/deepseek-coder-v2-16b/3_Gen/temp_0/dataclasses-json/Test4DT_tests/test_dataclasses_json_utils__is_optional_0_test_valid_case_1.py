
from dataclasses import dataclass
from typing import Optional, List, Any
import pytest
from dataclasses_json.utils import _is_optional, _issubclass_safe, _hasargs

@pytest.mark.parametrize("type_, expected", [
    (Optional[int], True),
    (List[int], False),
    (Any, True)
])
def test_valid_case_1(type_, expected):
    assert _is_optional(type_) == expected
