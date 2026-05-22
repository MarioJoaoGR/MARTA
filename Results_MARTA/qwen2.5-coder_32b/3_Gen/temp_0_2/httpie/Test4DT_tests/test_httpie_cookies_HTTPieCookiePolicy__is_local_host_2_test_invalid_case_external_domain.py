
import pytest
from unittest.mock import patch
from httpie.cookies import HTTPieCookiePolicy

def test_invalid_case_external_domain():
    policy = HTTPieCookiePolicy()
    
    with patch('httpie.cookies.HTTPieCookiePolicy._is_local_host', return_value=False):
        assert not policy._is_local_host('example.com')
