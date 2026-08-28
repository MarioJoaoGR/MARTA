
import pytest
import time
from httpie.utils import _max_age_to_expires

# Test cases for _max_age_to_expires function

def test_basic_usage():
    cookies = [{'name': 'session', 'max-age': '3600'}, {'name': 'user_token', 'expires': 1672502400}]
    now = time.time()
    _max_age_to_expires(cookies, now)
    assert cookies == [{'name': 'session', 'max-age': '3600', 'expires': now + float('3600')}, {'name': 'user_token', 'expires': 1672502400}]

def test_no_max_age():
    cookies = [{'name': 'user_token', 'expires': 1672502400}]
    now = time.time()
    _max_age_to_expires(cookies, now)
    assert cookies == [{'name': 'user_token', 'expires': 1672502400}]

def test_multiple_cookies():
    cookies = [
        {'name': 'session', 'max-age': '3600'},
        {'name': 'user_token', 'expires': 1672502400},
        {'name': 'remember_me', 'max-age': '86400'}
    ]
    now = time.time()
    _max_age_to_expires(cookies, now)
    assert cookies == [
        {'name': 'session', 'max-age': '3600', 'expires': now + float('3600')},
        {'name': 'user_token', 'expires': 1672502400},
        {'name': 'remember_me', 'max-age': '86400', 'expires': now + float('86400')}
    ]

def test_zero_max_age():
    cookies = [{'name': 'session', 'max-age': '0'}, {'name': 'user_token', 'expires': 1672502400}]
    now = time.time()
    _max_age_to_expires(cookies, now)