
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
    return [cookie.strip() for cookie in cookies.split(',')]

@pytest.mark.parametrize("cookies, expected", [
    ('cookie1=value1, cookie2=value2', ['cookie1=value1', 'cookie2=value2']),
    ('; path=/; domain=.example.com; Secure', ['; path=/; domain=.example.com; Secure']),
    ('', []),
])
def test_valid_input(cookies, expected):
    assert split_cookies(cookies) == expected
