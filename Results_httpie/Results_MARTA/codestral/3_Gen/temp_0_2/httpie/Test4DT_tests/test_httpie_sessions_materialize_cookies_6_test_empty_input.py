
import pytest
from httpie.sessions import materialize_cookie, materialize_cookies
from requests.cookies import RequestsCookieJar
from unittest.mock import patch
from typing import List, Dict, Any

def test_empty_input():
    empty_jar = RequestsCookieJar()
    
    with patch('httpie.sessions.materialize_cookie', side_effect=lambda x: {'name': x.name, 'value': x.value}):
        cookies_dicts = materialize_cookies(empty_jar)
        
        assert len(cookies_dicts) == 0
