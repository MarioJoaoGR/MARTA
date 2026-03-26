
import pytest

def test_valid_input_list():
    value = [' apple ', ' banana ', ' cherry ']
    expected_output = ['apple', 'banana', 'cherry']
    
    result = _as_list(value)
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings__as_list_1_test_valid_input_list
isort/Test4DT_tests/test_isort_settings__as_list_1_test_valid_input_list.py:8:13: E0602: Undefined variable '_as_list' (undefined-variable)


"""