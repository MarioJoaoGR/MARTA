
import pytest
from unittest.mock import patch, MagicMock
from httpie.sessions import materialize_cookie
from typing import Dict, Any

@pytest.fixture(autouse=True)
def mock_httpie_sessions():
    with patch('httpie.sessions.KEPT_COOKIE_OPTIONS', ['domain']):
        yield

class InvalidCookie:
    pass

def test_invalid_input():
    cookie = InvalidCookie()
    cookie._rest = {'is_explicit_none': True}
    
    with pytest.raises(AttributeError):
        materialize_cookie(cookie)
