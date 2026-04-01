
import pytest
from string_utils.validation import __ISBNChecker

def test_valid_isbn_13():
    # Test a valid ISBN-13 number with hyphens
    assert is_isbn_13('9780312498580') == True
    
    # Test a valid ISBN-13 number without hyphens, using the default normalize=True
    assert is_isbn_13('978-0312498580') == True
    
    # Test an invalid ISBN-13 number with hyphens and strict normalization check
    assert is_isbn_13('978-0312498580', normalize=False) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_isbn_13_0_test_valid_isbn_13
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_13_0_test_valid_isbn_13.py:7:11: E0602: Undefined variable 'is_isbn_13' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_13_0_test_valid_isbn_13.py:10:11: E0602: Undefined variable 'is_isbn_13' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_13_0_test_valid_isbn_13.py:13:11: E0602: Undefined variable 'is_isbn_13' (undefined-variable)


"""