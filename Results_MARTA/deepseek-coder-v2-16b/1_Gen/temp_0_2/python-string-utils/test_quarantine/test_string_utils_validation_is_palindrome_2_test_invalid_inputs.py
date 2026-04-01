
import pytest
from string_utils.validation import is_palindrome

def test_invalid_inputs():
    # Test case for invalid input types (non-string)
    assert not is_palindrome(12345)  # int should return False
    
    # Test case for empty string
    assert not is_palindrome("")  # Empty string should return False
    
    # Test case for string with only spaces
    assert not is_palindrome("   ")  # String with only spaces should return False
    
    # Test case for non-palindromic string (ignoring case)
    assert not is_palindrome("Hello", ignore_case=True)  # "Hello" should return False when ignoring case
    
    # Test case for non-palindromic string (with spaces)
    assert not is_palindrome("A man a plan a canal Panama", ignore_spaces=True, ignore_case=True)  # Should return False with given conditions

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test case for invalid input types (non-string)
        assert not is_palindrome(12345)  # int should return False
    
        # Test case for empty string
        assert not is_palindrome("")  # Empty string should return False
    
        # Test case for string with only spaces
        assert not is_palindrome("   ")  # String with only spaces should return False
    
        # Test case for non-palindromic string (ignoring case)
        assert not is_palindrome("Hello", ignore_case=True)  # "Hello" should return False when ignoring case
    
        # Test case for non-palindromic string (with spaces)
>       assert not is_palindrome("A man a plan a canal Panama", ignore_spaces=True, ignore_case=True)  # Should return False with given conditions
E       AssertionError: assert not True
E        +  where True = is_palindrome('A man a plan a canal Panama', ignore_spaces=True, ignore_case=True)

python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_2_test_invalid_inputs.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.03s ===============================
"""