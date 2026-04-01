
import pytest

def test_valid_input_lf():
    assert _infer_line_separator("Hello\nWorld") == "\n"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_parse__infer_line_separator_2_test_valid_input_lf
isort/Test4DT_tests/test_isort_parse__infer_line_separator_2_test_valid_input_lf.py:5:11: E0602: Undefined variable '_infer_line_separator' (undefined-variable)


"""