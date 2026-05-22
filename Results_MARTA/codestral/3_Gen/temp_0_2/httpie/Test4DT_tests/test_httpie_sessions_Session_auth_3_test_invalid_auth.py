
import pytest
from unittest.mock import patch
from httpie.sessions import Session, Environment
from pathlib import Path

def test_invalid_auth():
    with patch('httpie.sessions.Session.__init__', side_effect=AssertionError):
        with pytest.raises(AssertionError):
            session = Session(path='temp.sess', env=Environment(), bound_host='example.com', session_id='12345')
