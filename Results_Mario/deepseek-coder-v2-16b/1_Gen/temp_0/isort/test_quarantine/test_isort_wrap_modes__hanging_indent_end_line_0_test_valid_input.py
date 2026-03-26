
import pytest

def test_valid_input():
    line = "This is a test line."
    assert _hanging_indent_end_line(line) == "This is a test line. \\"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_wrap_modes__hanging_indent_end_line_0_test_valid_input
isort/Test4DT_tests/test_isort_wrap_modes__hanging_indent_end_line_0_test_valid_input.py:6:11: E0602: Undefined variable '_hanging_indent_end_line' (undefined-variable)


"""