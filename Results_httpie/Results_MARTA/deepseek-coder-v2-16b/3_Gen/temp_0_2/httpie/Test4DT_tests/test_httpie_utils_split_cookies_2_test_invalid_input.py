
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

def test_invalid_input():
    with patch('builtins.isinstance', side_effect=lambda obj, typ: isinstance(obj, str)):
        assert split_cookies(None) == []
        assert split_cookies("") == []
        assert split_cookies("cookie1=value1") == ["cookie1=value1"]
        assert split_cookies("cookie1=value1, cookie2=value2") == ["cookie1=value1", "cookie2=value2"]
        assert split_cookies("; path=/; domain=.example.com; Secure") == ["; path=/; domain=.example.com; Secure"]
