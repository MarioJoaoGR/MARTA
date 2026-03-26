
import pytest
from dataclasses_json.utils import _get_type_origin, List, Union

def test_edge_case_none():
    # Test when the type has no origin (should return the type itself)
    my_list = List[int]
    assert _get_type_origin(my_list) is my_list

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__get_type_origin_0_test_edge_case_none
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_edge_case_none.py:3:0: E0611: No name 'List' in module 'dataclasses_json.utils' (no-name-in-module)


"""