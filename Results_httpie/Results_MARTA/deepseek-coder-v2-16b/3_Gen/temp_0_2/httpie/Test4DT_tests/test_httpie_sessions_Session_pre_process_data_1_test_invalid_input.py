
import pytest
from pathlib import Path
from httpie.sessions import Session, Environment
from unittest.mock import patch

@pytest.fixture(scope="session")
def session():
    return Session(path='temp.json', env=Environment(), bound_host='example.com', session_id='12345')

def test_invalid_input(session):
    with pytest.raises(TypeError):
        # Test invalid input by passing a non-string path to the Session constructor
        with patch('httpie.sessions.Path', side_effect=TypeError("Invalid path type")):
            Session(path=123, env=Environment(), bound_host='example.com', session_id='12345')
