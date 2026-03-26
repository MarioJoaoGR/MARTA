
import pytest
from dataclasses_json.utils import _get_type_origin, List, Union

def test_edge_case_none():
    # Define a type with an origin that should be None for testing purposes
    my_list = List[int]
    
    # Test when the origin is actually None
    assert _get_type_origin(my_list) is None, "Expected None as the origin"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__get_type_origin_1_test_edge_case_none
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_1_test_edge_case_none.py:3:0: E0611: No name 'List' in module 'dataclasses_json.utils' (no-name-in-module)


"""