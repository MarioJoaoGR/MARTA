
import pytest
from string_utils.validation import is_full_string
from re import sub

SPACES_RE = sub(' ', '', '')

def is_palindrome(input_string: str, ignore_spaces: bool = False, ignore_case: bool = False) -> bool:
    """
    Checks if the string is a palindrome (https://en.wikipedia.org/wiki/Palindrome).

    *Examples:*

    >>> is_palindrome('LOL') # returns true
    >>> is_palindrome('Lol') # returns false
    >>> is_palindrome('Lol', ignore_case=True) # returns true
    >>> is_palindrome('ROTFL') # returns false

    :param input_string: String to check.
    :type input_string: str
    :param ignore_spaces: False if white spaces matter (default), true otherwise.
    :type ignore_spaces: bool
    :param ignore_case: False if char case matters (default), true otherwise.
    :type ignore_case: bool
    :return: True if the string is a palindrome (like "otto", or "i topi non avevano nipoti" if strict=False),\
    False otherwise
    """
    if not is_full_string(input_string):
        return False

    if ignore_spaces:
        input_string = sub(' ', '', input_string)

    string_len = len(input_string)

    # Traverse the string one char at step, and for each step compares the
    # "head_char" (the one on the left of the string) to the "tail_char" (the one on the right).
    # In this way we avoid to manipulate the whole string in advance if not necessary and provide a faster
    # algorithm which can scale very well for long strings.
    for index in range(string_len):
        head_char = input_string[index]
        tail_char = input_string[string_len - index - 1]

        if ignore_case:
            head_char = head_char.lower()
            tail_char = tail_char.lower()

        if head_char != tail_char:
            return False

    return True

def test_edge_cases():
    # Test for None input
    assert not is_palindrome(None)
    
    # Test for empty string
    assert is_palindrome('')
    
    # Test for non-palindromes
    assert not is_palindrome('hello')
    assert not is_palindrome('world')
    
    # Test for palindromes with different cases and spaces handling
    assert is_palindrome('LOL', ignore_case=True)
    assert not is_palindrome('Lol')
    assert is_palindrome('i topi non avevano nipoti', ignore_spaces=True, ignore_case=True)

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
        # Test for None input
        assert not is_palindrome(None)
    
        # Test for empty string
>       assert is_palindrome('')
E       AssertionError: assert False
E        +  where False = is_palindrome('')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_1_test_edge_cases.py:58: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_palindrome_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.03s ===============================
"""