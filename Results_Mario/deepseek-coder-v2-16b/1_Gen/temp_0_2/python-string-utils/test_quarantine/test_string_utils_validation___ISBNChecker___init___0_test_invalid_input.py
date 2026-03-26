
import pytest
from string_utils.validation import InvalidInputError
from python_string_utils.__ISBNChecker import __ISBNChecker

def test_invalid_input():
    with pytest.raises(InvalidInputError) as exc_info:
        checker = __ISBNChecker(12345)  # Providing an integer instead of a string
    
    assert str(exc_info.value) == "Expected 'str', received <class 'int'>"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation___ISBNChecker___init___0_test_invalid_input
python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___0_test_invalid_input.py:4:0: E0401: Unable to import 'python_string_utils.__ISBNChecker' (import-error)


"""