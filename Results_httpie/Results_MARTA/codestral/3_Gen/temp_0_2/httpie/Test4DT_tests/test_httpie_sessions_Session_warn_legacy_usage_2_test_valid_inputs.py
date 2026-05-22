
import pytest
from httpie.sessions import Session, Environment
from pathlib import Path
from unittest.mock import patch

@pytest.fixture
def setup_session():
    env = Environment()
    session = Session(
        path=Path('test_session'),
        env=env,
        bound_host='example.com',
        session_id='unique_id'
    )
    return session

def test_valid_inputs(setup_session):
    session = setup_session
    
    # Check if the session object is initialized correctly
    assert isinstance(session, Session)
    assert session['headers'] == []
    assert session['cookies'] == []
    assert session['auth'] == {'type': None, 'username': None, 'password': None}
    assert session.env == setup_session.env
    assert session._headers == setup_session._headers
    assert session.cookie_jar == setup_session.cookie_jar
    assert session.session_id == 'unique_id'
    assert session.bound_host == 'example.com'
