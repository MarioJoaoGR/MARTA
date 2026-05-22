
import pytest
from unittest.mock import patch, MagicMock
from httpie.sessions import Session
from httpie.sessions import Environment

@pytest.fixture
def session():
    return Session(path='session_data.json', env=Environment(), bound_host='example.com', session_id='12345')

def test_add_cookies(session):
    cookies = [{'name': 'user_cookie', 'value': 'user_value'}]
    
    with patch('httpie.sessions.RequestsCookieJar.set') as mock_set:
        session._add_cookies(cookies)
        
        assert mock_set.call_count == 1
        call_args = mock_set.call_args[1]
        assert call_args['name'] == 'user_cookie'
        assert call_args['value'] == 'user_value'
