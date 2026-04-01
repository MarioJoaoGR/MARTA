
import pytest
from your_module import _is_new_type_subclass_safe  # Replace 'your_module' with the actual module name where the function is defined

def test_edge_case_none():
    assert not _is_new_type_subclass_safe(None, int)
    assert not _is_new_type_subclass_safe(int, None)
    assert not _is_new_type_subclass_safe(None, None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_new_type_subclass_safe_1_test_edge_case_none
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_subclass_safe_1_test_edge_case_none.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""