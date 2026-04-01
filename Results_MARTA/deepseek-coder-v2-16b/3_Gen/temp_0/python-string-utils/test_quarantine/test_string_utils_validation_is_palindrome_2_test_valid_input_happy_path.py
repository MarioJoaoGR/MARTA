
import pytest
from string_utils.validation import is_palindrome

def test_valid_input_happy_path():
    # Test palindromes without ignoring any character
    assert is_palindrome('LOL') == True
    assert is_palindrome('radar') == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True  # Case sensitive but still a palindrome
    
    # Test palindromes with case sensitivity ignored
    assert is_palindrome('Lol', ignore_case=True) == True
    assert is_palindrome("A man, a plan, a canal: Panama", ignore_case=True) == True
    
    # Test non-palindromes
    assert is_palindrome('ROTFL') == False
    assert is_palindrome('hello') == False
    assert is_palindrome("This is not a palindrome") == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_2_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        # Test palindromes without ignoring any character
        assert is_palindrome('LOL') == True
        assert is_palindrome('radar') == True
>       assert is_palindrome("A man, a plan, a canal: Panama") == True  # Case sensitive but still a palindrome
E       AssertionError: assert False == True
E        +  where False = is_palindrome('A man, a plan, a canal: Panama')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_2_test_valid_input_happy_path.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_2_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.03s ===============================
"""