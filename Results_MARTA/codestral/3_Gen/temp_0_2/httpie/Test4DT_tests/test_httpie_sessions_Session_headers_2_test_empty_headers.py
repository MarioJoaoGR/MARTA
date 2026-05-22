
import pytest
from pathlib import Path
from httpie.sessions import Environment, Session
from unittest.mock import patch

@pytest.fixture(scope="function")
def setup_session():
    env = Environment()
    session = Session(path=Path('session_file'), env=env, bound_host='example.com', session_id='12345')
    return session

def test_empty_headers(setup_session):
    with patch('httpie.sessions.Session.__init__', side_effect=None):
        assert setup_session['headers'] == []
