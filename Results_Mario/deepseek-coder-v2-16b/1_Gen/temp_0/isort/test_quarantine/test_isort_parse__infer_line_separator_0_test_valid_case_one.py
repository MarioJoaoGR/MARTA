
import pytest

def test_valid_case_one():
    # Test case with "\r\n" as separator
    contents = "Line 1\r\nLine 2\r\nLine 3"
    assert _infer_line_separator(contents) == "\r\n"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_parse__infer_line_separator_0_test_valid_case_one
isort/Test4DT_tests/test_isort_parse__infer_line_separator_0_test_valid_case_one.py:7:11: E0602: Undefined variable '_infer_line_separator' (undefined-variable)


"""