
import pytest
from unittest.mock import patch
from httpie.utils import RE_COOKIE_SPLIT

def split_cookies(cookies):
    """
    When ``requests`` stores cookies in ``response.headers['Set-Cookie']``
    it concatenates all of them through ``, ``.

    This function splits cookies apart being careful to not to
    split on ``, `` which may be part of cookie value.
    """
    if not cookies:
        return []
    return RE_COOKIE_SPLIT.split(cookies)

@pytest.mark.parametrize("input_cookies, expected", [
    ('cookie1=value1, cookie2=value2', ['cookie1=value1', 'cookie2=value2']),
    ('; path=/; domain=.example.com; Secure', ['; path=/; domain=.example.com; Secure']),
    ('', []),
    (None, [])
])
def test_split_cookies(input_cookies, expected):
    with patch('httpie.utils.RE_COOKIE_SPLIT', None):  # Assuming RE_COOKIE_SPLIT is a global variable or module attribute
        assert split_cookies(input_cookies) == expected
