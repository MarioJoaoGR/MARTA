
import pytest

def test_valid_case_one():
    assert _infer_line_separator("Hello\r\nWorld") == "\r\n"
    assert _infer_line_separator("Hello\rWorld") == "\r"
    assert _infer_line_separator("Hello\nWorld") == "\n"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_parse__infer_line_separator_0_test_valid_case_one
isort/Test4DT_tests/test_isort_parse__infer_line_separator_0_test_valid_case_one.py:5:11: E0602: Undefined variable '_infer_line_separator' (undefined-variable)
isort/Test4DT_tests/test_isort_parse__infer_line_separator_0_test_valid_case_one.py:6:11: E0602: Undefined variable '_infer_line_separator' (undefined-variable)
isort/Test4DT_tests/test_isort_parse__infer_line_separator_0_test_valid_case_one.py:7:11: E0602: Undefined variable '_infer_line_separator' (undefined-variable)


"""