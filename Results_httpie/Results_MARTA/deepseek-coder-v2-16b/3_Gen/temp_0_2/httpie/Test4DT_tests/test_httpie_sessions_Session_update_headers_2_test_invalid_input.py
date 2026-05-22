
import pytest
from pathlib import Path
from httpie.sessions import Session, Environment
from unittest.mock import patch

@pytest.fixture(scope="session")
def session():
    return Session(path=Path('session_data'), env=Environment(), bound_host='example.com', session_id='12345')

def test_invalid_input(session):
    with patch('httpie.sessions.Session.__init__', side_effect=TypeError("Invalid input type")):
        with pytest.raises(TypeError, match="Invalid input type"):
            Session(path=123, env=Environment(), bound_host='example.com', session_id='12345')
