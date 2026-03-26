
import pytest
from hanging_indent import hanging_indent

def test_edge_case_none():
    with pytest.raises(TypeError):
        hanging_indent()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_wrap_modes_hanging_indent_0_test_edge_case_none
isort/Test4DT_tests/test_isort_wrap_modes_hanging_indent_0_test_edge_case_none.py:3:0: E0401: Unable to import 'hanging_indent' (import-error)


"""