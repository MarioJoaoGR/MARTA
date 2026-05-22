
import pytest
from httpie.sessions import materialize_cookies, materialize_cookie
from requests.cookies import RequestsCookieJar
from unittest.mock import patch
from typing import List, Dict, Any

@pytest.mark.parametrize("jar", [RequestsCookieJar()])
def test_valid_input(jar):
    with patch('requests.cookies.RequestsCookieJar') as mock_jar:
        mock_jar.return_value = jar
        cookies_dicts = materialize_cookies(mock_jar.return_value)
        assert isinstance(cookies_dicts, list), "Expected a list of dictionaries"
        for cookie_dict in cookies_dicts:
            assert isinstance(cookie_dict, dict), "Each item should be a dictionary"
            assert 'name' in cookie_dict, "Every cookie must have a name"
            assert 'value' in cookie_dict, "Every cookie must have a value"
