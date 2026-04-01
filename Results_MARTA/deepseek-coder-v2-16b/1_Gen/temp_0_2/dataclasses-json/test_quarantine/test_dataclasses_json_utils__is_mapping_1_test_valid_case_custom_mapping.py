
import pytest
from collections.abc import Mapping
from typing import get_origin

def _is_mapping(type_):
    return issubclass(_get_type_origin(type_), Mapping)

def test_valid_case_custom_mapping():
    class MyDict(dict): pass
    
    assert _is_mapping(MyDict) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_mapping_1_test_valid_case_custom_mapping
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_1_test_valid_case_custom_mapping.py:7:22: E0602: Undefined variable '_get_type_origin' (undefined-variable)


"""