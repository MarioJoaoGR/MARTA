
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.sessions import upgrade_session, ExitStatus

class TestUpgradeSession(unittest.TestCase):
    
    @patch('httpie.manager.tasks.sessions.get_httpie_session')
    def test_valid_inputs(self, mock_get_httpie_session):
        env = MagicMock()
        args = MagicMock()
        hostname = 'example.com'
        session_name = 'session123'
        
        # Mock the get_httpie_session to return a mock session object
        mock_get_httpie_session.return_value = MagicMock(is_new=lambda: False, version='0.9')
        
        # Call the function under test
        result = upgrade_session(env, args, hostname, session_name)
        
        # Assert that the necessary methods were called on the mock objects
        mock_get_httpie_session.assert_called_once_with(
            env=env,
            config_dir=env.config.directory,
            session_name=session_name,
            host=hostname,
            url=hostname,
            suppress_legacy_warnings=True
        )
        
        # Assert that the fixers were applied correctly
        self.assertEqual(result, ExitStatus.SUCCESS)
