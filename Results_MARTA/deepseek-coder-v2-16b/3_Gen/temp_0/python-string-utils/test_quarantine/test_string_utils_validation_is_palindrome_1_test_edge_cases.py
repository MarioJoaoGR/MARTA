
import pytest
from string_utils.validation import is_palindrome

def test_edge_cases():
    # Test cases for empty strings
    assert not is_palindrome("")
    
    # Test cases for single character strings
    assert is_palindrome("a")
    assert is_palindrome("b")
    assert not is_palindrome("c")

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
        # Test cases for empty strings
        assert not is_palindrome("")
    
        # Test cases for single character strings
        assert is_palindrome("a")
        assert is_palindrome("b")
>       assert not is_palindrome("c")
E       AssertionError: assert not True
E        +  where True = is_palindrome('c')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_1_test_edge_cases.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.02s ===============================
"""