
import pytest
from unittest.mock import patch
from httpie.cookies import HTTPieCookiePolicy

def test_valid_case_localhost():
    policy = HTTPieCookiePolicy()
    with patch('httpie.cookies.HTTPieCookiePolicy._is_local_host', return_value=True):
        assert policy._is_local_host('localhost') is True
