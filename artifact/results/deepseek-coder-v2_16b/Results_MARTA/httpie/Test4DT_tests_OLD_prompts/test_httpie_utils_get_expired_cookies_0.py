
import pytest
from unittest.mock import patch
import time
from httpie.utils import get_expired_cookies


def test_without_specific_time():
    headers = [('Set-Cookie', 'cookie1=value1; expires=Tue, 08 Jan 2024 12:00:00 GMT'), ('Set-Cookie', 'cookie2=value2; path=/')]
    with patch('time.time', return_value=time.time()):
        expired_cookies = get_expired_cookies(headers)
        assert len(expired_cookies) == 1, "Expected one expired cookie but got none."

def test_no_expiration_info():
    headers = [('Set-Cookie', 'cookie1=value1'), ('Set-Cookie', 'cookie2=value2; expires=Tue, 08 Jan 2024 12:00:00 GMT')]
    with patch('time.time', return_value=time.time()):
        expired_cookies = get_expired_cookies(headers)
        assert len(expired_cookies) == 1, "Expected one expired cookie but got none."