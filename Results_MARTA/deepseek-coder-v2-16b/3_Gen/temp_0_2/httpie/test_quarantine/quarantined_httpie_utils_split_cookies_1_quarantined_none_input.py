
import pytest
from unittest.mock import patch
from httpie.utils import RE_COOKIE_SPLIT

@pytest.mark.parametrize("input_cookies, expected", [
    ('cookie1=value1, cookie2=value2', ['cookie1=value1', 'cookie2=value2']),
    ('; path=/; domain=.example.com; Secure', ['; path=/; domain=.example.com; Secure']),
    ('', []),
    (None, [])
])
def test_split_cookies(input_cookies, expected):
    with patch('httpie.utils.RE_COOKIE_SPLIT', None):  # Assuming RE_COOKIE_SPLIT is a global variable or module attribute
        assert split_cookies(input_cookies) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_utils_split_cookies_1_test_none_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_split_cookies_1_test_none_input.py:14:15: E0602: Undefined variable 'split_cookies' (undefined-variable)


"""