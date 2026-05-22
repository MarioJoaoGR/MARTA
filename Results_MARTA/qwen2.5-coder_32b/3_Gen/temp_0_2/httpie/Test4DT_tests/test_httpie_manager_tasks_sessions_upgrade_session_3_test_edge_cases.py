
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.sessions import upgrade_session, Environment, ExitStatus, get_httpie_session

@pytest.fixture(autouse=True)
def mock_dependencies():
    with patch('httpie.manager.tasks.sessions.get_httpie_session', return_value=MagicMock()):
        yield

def test_upgrade_session_none_inputs():
    env = Environment()
    args = MagicMock()
    hostname = None
    session_name = None
    
    result = upgrade_session(env, args, hostname, session_name)
    
    assert result == ExitStatus.ERROR
