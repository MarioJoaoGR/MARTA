
import pytest
from httpie.sessions import materialize_cookie, materialize_cookies
from requests.cookies import RequestsCookieJar
from typing import List, Dict, Any
from unittest.mock import patch

def test_empty_input():
    jar = RequestsCookieJar()
    with patch('httpie.sessions.materialize_cookie', side_effect=lambda x: {'name': x.name, 'value': x.value}):
        cookies_dicts = materialize_cookies(jar)
        assert cookies_dicts == []
