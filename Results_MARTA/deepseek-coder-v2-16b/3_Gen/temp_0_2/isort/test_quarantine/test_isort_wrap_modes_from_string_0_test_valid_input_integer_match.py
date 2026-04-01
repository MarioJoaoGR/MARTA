
import pytest
from isort.wrap_modes import WrapModes

def test_valid_input_integer_match():
    # Test cases for valid integer matches
    assert from_string('1') == WrapModes(1)
    assert from_string('2') == WrapModes(2)
    assert from_string('3') == WrapModes(3)
    
    # Additional test case to ensure it handles invalid inputs gracefully
    assert from_string('invalid') is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_wrap_modes_from_string_0_test_valid_input_integer_match
isort/Test4DT_tests/test_isort_wrap_modes_from_string_0_test_valid_input_integer_match.py:7:11: E0602: Undefined variable 'from_string' (undefined-variable)
isort/Test4DT_tests/test_isort_wrap_modes_from_string_0_test_valid_input_integer_match.py:8:11: E0602: Undefined variable 'from_string' (undefined-variable)
isort/Test4DT_tests/test_isort_wrap_modes_from_string_0_test_valid_input_integer_match.py:9:11: E0602: Undefined variable 'from_string' (undefined-variable)
isort/Test4DT_tests/test_isort_wrap_modes_from_string_0_test_valid_input_integer_match.py:12:11: E0602: Undefined variable 'from_string' (undefined-variable)


"""