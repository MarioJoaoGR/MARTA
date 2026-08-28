
import pytest
from httpie.utils import get_expired_cookies
from typing import List, Tuple


def test_basic_usage():
    headers = [('Set-Cookie', 'cookie1=value1; expires=Tue, 08 Jan 2024 12:00:00 GMT'), ('Set-Cookie', 'cookie2=value2; path=/')]
    expired_cookies = get_expired_cookies(headers)
    assert len(expired_cookies) == 1
    assert expired_cookies[0]['name'] == 'cookie1'

def test_specific_time():
    import time
    headers = [('Set-Cookie', 'cookie1=value1; expires=Tue, 08 Jan 2024 12:00:00 GMT'), ('Set-Cookie', 'cookie2=value2; path=/')]
    now = time.time()
    expired_cookies = get_expired_cookies(headers, now)
    assert len(expired_cookies) == 1
    assert expired_cookies[0]['name'] == 'cookie1'

def test_no_expiry_information():
    headers = [('Set-Cookie', 'cookie1=value1'), ('Set-Cookie', 'cookie2=value2; expires=Tue, 08 Jan 2024 12:00:00 GMT')]
    expired_cookies = get_expired_cookies(headers)
    assert len(expired_cookies) == 1
    assert expired_cookies[0]['name'] == 'cookie2'