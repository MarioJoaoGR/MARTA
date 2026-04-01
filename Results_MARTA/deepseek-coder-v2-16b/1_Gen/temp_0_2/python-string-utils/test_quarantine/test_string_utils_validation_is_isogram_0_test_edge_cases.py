
import pytest
from string_utils.validation import is_full_string

def test_edge_cases():
    # Test None input
    assert not is_isogram(None)
    
    # Test empty string
    assert is_isogram("")
    
    # Test single character string
    assert is_isogram("a")
    
    # Test string with spaces and hyphens
    assert is_isogram("dermatoglyphics")
    assert not is_isogram("hello world")
    
    # Test case insensitivity
    assert is_isogram("Dermatoglyphics")
    assert not is_isogram("Hello")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_isogram_0_test_edge_cases
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_0_test_edge_cases.py:7:15: E0602: Undefined variable 'is_isogram' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_0_test_edge_cases.py:10:11: E0602: Undefined variable 'is_isogram' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_0_test_edge_cases.py:13:11: E0602: Undefined variable 'is_isogram' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_0_test_edge_cases.py:16:11: E0602: Undefined variable 'is_isogram' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_0_test_edge_cases.py:17:15: E0602: Undefined variable 'is_isogram' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_0_test_edge_cases.py:20:11: E0602: Undefined variable 'is_isogram' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_0_test_edge_cases.py:21:15: E0602: Undefined variable 'is_isogram' (undefined-variable)


"""