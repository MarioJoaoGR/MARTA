
import pytest
from dataclasses_json.core import _is_supported_generic, _issubclass_safe, _is_collection, _is_optional, is_union_type, _is_generic_dataclass
from typing import List, Optional, Union, Enum, Any
from dataclasses import dataclass

@pytest.mark.parametrize("type_, expected", [
    (List[int], True),
    (Optional[int], True),
    (Union[int, str], True),
    (Enum, False),  # Assuming Enum is not a subclass of any type in this context
    (Any, True)     # Any can be considered as supported since it's a special type
])
def test_is_supported_generic(type_, expected):
    assert _is_supported_generic(type_) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__is_supported_generic_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__is_supported_generic_0_test_edge_cases.py:4:0: E0611: No name 'Enum' in module 'typing' (no-name-in-module)


"""