
import pytest
from unittest.mock import patch
from httpie.utils import split_cookies

@pytest.mark.parametrize("input_string, expected", [
    ('cookie1=value1, cookie2=value2', ['cookie1=value1', 'cookie2=value2']),
    ('; path=/; domain=.example.com; Secure', ['; path=/; domain=.example.com; Secure']),
    ('', [])
])
def test_split_cookies(input_string, expected):
    with patch('httpie.utils.RE_COOKIE_SPLIT', re.compile(r',\s*')):
        assert split_cookies(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_utils_split_cookies_1_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_split_cookies_1_test_valid_input.py:12:47: E0602: Undefined variable 're' (undefined-variable)


"""