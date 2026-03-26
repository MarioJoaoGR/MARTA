
import pytest

def test_valid_case_three():
    # Test case with '\n' as separator
    contents = "Line 1\nLine 2\nLine 3"
    assert _infer_line_separator(contents) == "\n"

    # Additional test cases to ensure robustness
    assert _infer_line_separator("Line 1\rLine 2\rLine 3") == "\r"
    assert _infer_line_separator("Line 1\r\nLine 2\r\nLine 3") == "\r\n"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_parse__infer_line_separator_2_test_valid_case_three
isort/Test4DT_tests/test_isort_parse__infer_line_separator_2_test_valid_case_three.py:7:11: E0602: Undefined variable '_infer_line_separator' (undefined-variable)
isort/Test4DT_tests/test_isort_parse__infer_line_separator_2_test_valid_case_three.py:10:11: E0602: Undefined variable '_infer_line_separator' (undefined-variable)
isort/Test4DT_tests/test_isort_parse__infer_line_separator_2_test_valid_case_three.py:11:11: E0602: Undefined variable '_infer_line_separator' (undefined-variable)


"""