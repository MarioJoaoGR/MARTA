
import pytest
from httpie.sessions import Session
from httpie.sessions import Environment
from pathlib import Path
from typing import List, Dict, Any
from unittest.mock import patch

@pytest.fixture
def session():
    return Session(path=Path('session_data.json'), env=Environment(), bound_host='example.com', session_id='12345')

def test_add_cookies(session):
    cookies = [{'name': 'user_cookie', 'value': 'user_value'}]
    
    with patch('httpie.sessions.RequestsCookieJar.set'):
        session._add_cookies(cookies)
