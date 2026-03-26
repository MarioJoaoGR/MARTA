
import pytest
from string_utils.validation import is_full_string

def test_not_pangram():
    # Test a non-pangram sentence
    assert not is_pangram('hello world')
    
    # Add more tests if needed to cover different scenarios or edge cases

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_pangram_6_test_not_pangram
python-string-utils/Test4DT_tests/test_string_utils_validation_is_pangram_6_test_not_pangram.py:7:15: E0602: Undefined variable 'is_pangram' (undefined-variable)


"""