
import pytest
from unittest.mock import patch
from httpie.cookies import _LOCALHOST, _LOCALHOST_SUFFIX
from httpie.cookies import HTTPieCookiePolicy

def test_valid_case_localhost():
    policy = HTTPieCookiePolicy()
    with patch('httpie.cookies._LOCALHOST', 'localhost'):
        with patch('httpie.cookies._LOCALHOST_SUFFIX', ''):
            assert policy._is_local_host('localhost') == True
