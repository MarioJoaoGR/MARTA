
import pytest
from httpie.sessions import materialize_cookies
from requests.cookies import RequestsCookieJar
from unittest.mock import patch, MagicMock
from typing import List, Dict, Any

@pytest.fixture
def valid_jar():
    jar = RequestsCookieJar()
    # Assuming `jar` is populated with Cookie instances for testing purposes
    return jar

def test_valid_input(valid_jar):
    with patch('httpie.sessions.materialize_cookie', side_effect=lambda x: {'name': x.name, 'value': x.value}):
        cookies_dicts = materialize_cookies(valid_jar)
        assert isinstance(cookies_dicts, list), "Expected a list of dictionaries"
        for cookie_dict in cookies_dicts:
            assert isinstance(cookie_dict, dict), "Each item should be a dictionary"
            assert 'name' in cookie_dict and 'value' in cookie_dict, "Dictionary should contain 'name' and 'value'"
