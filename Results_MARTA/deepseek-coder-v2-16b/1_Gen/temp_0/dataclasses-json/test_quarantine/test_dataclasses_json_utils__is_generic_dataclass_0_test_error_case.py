
from dataclasses import is_dataclass
from dataclasses_json.utils import _get_type_origin
import pytest
from typing import List, Union

def test_error_case():
    my_list = List[int]
    mixed_types = Union[int, str]
    
    assert not _is_generic_dataclass(my_list)  # Assuming List[int] is not a dataclass by default
    assert not _is_generic_dataclass(mixed_types)  # Assuming Union[int, str] is not a dataclass by default

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_generic_dataclass_0_test_error_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_error_case.py:11:15: E0602: Undefined variable '_is_generic_dataclass' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_generic_dataclass_0_test_error_case.py:12:15: E0602: Undefined variable '_is_generic_dataclass' (undefined-variable)

"""