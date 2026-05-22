
import pytest
from unittest.mock import patch

def split_cookies(cookies):
    """
    When ``requests`` stores cookies in ``response.headers['Set-Cookie']``
    it concatenates all of them through ``, ``.

    This function splits cookies apart being careful to not to
    split on ``, `` which may be part of cookie value.
    """
    if not cookies:
        return []
    return [cookie.strip() for cookie in cookies.split(',') if cookie.strip()]

def test_valid_input():
    # Test with a valid cookies string
    assert split_cookies('cookie1=value1, cookie2=value2') == ['cookie1=value1', 'cookie2=value2']
    
    # Test with another valid cookies string
    assert split_contents = split_cookies('; path=/; domain=.example.com; Secure') == ['; path=/; domain=.example.com; Secure']
    
    # Test with an empty string
    assert split_cookies('') == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_utils_split_cookies_1_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_utils_split_cookies_1_test_valid_input.py:22:27: E0001: Parsing failed: 'invalid syntax (Test4DT_tests_codestral.test_httpie_utils_split_cookies_1_test_valid_input, line 22)' (syntax-error)


"""