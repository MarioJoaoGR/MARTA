
import pytest
from string_utils.validation import is_palindrome

def test_edge_cases():
    # Test cases for empty strings, single characters, and palindromes with different spacings and case sensitivity
    
    assert is_palindrome('') == False  # Empty string should not be a palindrome
    assert is_palindrome('a') == True   # Single character string is always a palindrome
    assert is_palindrome('LOL') == True # Case-sensitive palindrome
    assert is_palindrome('Lol', ignore_case=True) == True  # Case-insensitive palindrome
    assert is_palindrome('ROTFL') == False  # Not a palindrome due to different characters at the same position
    assert is_palindrome('No lemon, no melon') == True  # Palindrome ignoring spaces and case
    assert is_palindrome('Was it a car or a cat I saw?') == False  # Not a palindrome due to punctuation and spaces
    assert is_palindrome('Was it a car or a cat I saw?', ignore_spaces=True) == True  # Palindrome ignoring spaces but case-sensitive
    assert is_palindrome('Was it a car or a cat I saw?', ignore_case=True, ignore_spaces=True) == True  # Case-insensitive palindrome ignoring spaces

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test cases for empty strings, single characters, and palindromes with different spacings and case sensitivity
    
        assert is_palindrome('') == False  # Empty string should not be a palindrome
        assert is_palindrome('a') == True   # Single character string is always a palindrome
        assert is_palindrome('LOL') == True # Case-sensitive palindrome
        assert is_palindrome('Lol', ignore_case=True) == True  # Case-insensitive palindrome
        assert is_palindrome('ROTFL') == False  # Not a palindrome due to different characters at the same position
>       assert is_palindrome('No lemon, no melon') == True  # Palindrome ignoring spaces and case
E       AssertionError: assert False == True
E        +  where False = is_palindrome('No lemon, no melon')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_1_test_edge_cases.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.03s ===============================
"""