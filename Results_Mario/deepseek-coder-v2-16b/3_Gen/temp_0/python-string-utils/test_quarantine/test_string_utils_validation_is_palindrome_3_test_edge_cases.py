
import pytest
from string_utils.validation import is_full_string

def test_edge_cases():
    # Test None input
    assert not is_palindrome(None)
    
    # Test empty string
    assert is_palindrome("")
    
    # Test single character (should be a palindrome)
    assert is_palindrome("a")
    
    # Test non-palindrome with different case (case sensitive, should return False)
    assert not is_palindrome("Lol")
    
    # Test palindrome with ignore_case=True (should return True)
    assert is_palindrome("Lol", ignore_case=True)
    
    # Test non-palindrome string
    assert not is_palindrome("ROTFL")
    
    # Test palindrome with spaces and case insensitive
    assert is_palindrome("A man a plan a canal Panama", ignore_spaces=True, ignore_case=True)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_palindrome_3_test_edge_cases
python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_3_test_edge_cases.py:7:15: E0602: Undefined variable 'is_palindrome' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_3_test_edge_cases.py:10:11: E0602: Undefined variable 'is_palindrome' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_3_test_edge_cases.py:13:11: E0602: Undefined variable 'is_palindrome' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_3_test_edge_cases.py:16:15: E0602: Undefined variable 'is_palindrome' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_3_test_edge_cases.py:19:11: E0602: Undefined variable 'is_palindrome' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_3_test_edge_cases.py:22:15: E0602: Undefined variable 'is_palindrome' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_3_test_edge_cases.py:25:11: E0602: Undefined variable 'is_palindrome' (undefined-variable)


"""