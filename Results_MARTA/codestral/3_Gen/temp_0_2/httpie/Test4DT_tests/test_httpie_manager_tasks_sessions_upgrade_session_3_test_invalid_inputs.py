
import unittest
from unittest.mock import patch, MagicMock
from httpie.sessions import Environment
from httpie.manager.tasks.sessions import upgrade_session, ExitStatus

def test_invalid_inputs():
    env = Environment()
    args = MagicMock()
    hostname = 'example.com'
    
    # Test case for invalid session name (None)
    with patch('httpie.manager.tasks.sessions.get_httpie_session', return_value=MagicMock(is_new=lambda: True)):
        result = upgrade_session(env, args, hostname, None)
        assert result == ExitStatus.ERROR
    
    # Test case for invalid hostname (None)
    with patch('httpie.manager.tasks.sessions.get_httpie_session', return_value=MagicMock(is_new=lambda: True)):
        result = upgrade_session(env, args, None, 'session123')
        assert result == ExitStatus.ERROR
    
    # Test case for invalid session name (empty string)
    with patch('httpie.manager.tasks.sessions.get_httpie_session', return_value=MagicMock(is_new=lambda: True)):
        result = upgrade_session(env, args, hostname, '')
        assert result == ExitStatus.ERROR
    
    # Test case for invalid hostname (empty string)
    with patch('httpie.manager.tasks.sessions.get_httpie_session', return_value=MagicMock(is_new=lambda: True)):
        result = upgrade_session(env, args, '', 'session123')
        assert result == ExitStatus.ERROR
    
    # Test case for valid inputs (should pass)
    with patch('httpie.manager.tasks.sessions.get_httpie_session', return_value=MagicMock(is_new=lambda: False)):
        result = upgrade_session(env, args, hostname, 'session123')
        assert result == ExitStatus.SUCCESS
