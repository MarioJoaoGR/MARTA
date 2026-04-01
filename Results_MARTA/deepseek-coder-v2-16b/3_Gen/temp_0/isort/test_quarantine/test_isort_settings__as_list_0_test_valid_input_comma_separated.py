
import pytest

def test_valid_input_comma_separated():
    value = "apple, banana, orange"
    expected_output = ["apple", "banana", "orange"]
    assert _as_list(value) == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings__as_list_0_test_valid_input_comma_separated
isort/Test4DT_tests/test_isort_settings__as_list_0_test_valid_input_comma_separated.py:7:11: E0602: Undefined variable '_as_list' (undefined-variable)


"""