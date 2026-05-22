
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.sessions import Environment, get_httpie_session, ExitStatus, FIXERS_TO_VERSIONS, is_version_greater

@pytest.fixture(autouse=True)
def mock_environment():
    with patch('httpie.manager.tasks.sessions.Environment') as MockEnvironment:
        env = MockEnvironment.return_value
        yield env

@pytest.fixture(autouse=True)
def mock_session():
    with patch('httpie.manager.tasks.sessions.get_httpie_session') as MockSession:
        session = MagicMock()
        session.path.stem = 'my_session'
        session.is_new.return_value = False
        session.version = '1.0.0'
        MockSession.return_value = session
        yield MockSession

@pytest.fixture(autouse=True)
def mock_fixers():
    with patch('httpie.manager.tasks.sessions.FIXERS_TO_VERSIONS', {
        '2.0.0': MagicMock(),
        '1.5.0': MagicMock()
    }) as MockFixers:
        yield MockFixers

def test_valid_inputs():
    from httpie.manager.tasks.sessions import upgrade_session
    
    env = Environment()
    args = MagicMock()
    hostname = 'api.example.com'
    session_name = 'my_session'
    
    result = upgrade_session(env, args, hostname, session_name)
    
    assert result == ExitStatus.SUCCESS
