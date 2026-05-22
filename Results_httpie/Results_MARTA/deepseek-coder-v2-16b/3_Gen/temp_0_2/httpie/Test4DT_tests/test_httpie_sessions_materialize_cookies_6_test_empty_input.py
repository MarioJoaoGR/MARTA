
import pytest
from httpie.sessions import materialize_cookie, materialize_cookies
from requests.cookies import RequestsCookieJar
from typing import List, Dict, Any
from unittest.mock import patch

@pytest.fixture(name="empty_jar")
def fixture_empty_jar():
    return RequestsCookieJar()

def test_empty_input(empty_jar):
    with patch('httpie.sessions.materialize_cookie', side_effect=lambda x: {'name': x.name, 'value': x.value}):
        cookies_dicts = materialize_cookies(empty_jar)
        assert cookies_dicts == []
