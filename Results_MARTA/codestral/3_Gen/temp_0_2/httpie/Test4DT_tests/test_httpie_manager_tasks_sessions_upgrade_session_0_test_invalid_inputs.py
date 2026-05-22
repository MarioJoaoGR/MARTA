
import unittest
from unittest.mock import patch, MagicMock
from httpie.sessions import Environment
from httpie.manager.tasks.sessions import upgrade_session, ExitStatus

def test_invalid_inputs():
    env = Environment()
    args = MagicMock()
    hostname = None  # Invalid input: should be a string
    session_name = "example"

    with patch('httpie.manager.tasks.sessions.get_httpie_session', return_value=MagicMock(is_new=lambda: True)):
        result = upgrade_session(env, args, hostname, session_name)
        assert result == ExitStatus.ERROR
