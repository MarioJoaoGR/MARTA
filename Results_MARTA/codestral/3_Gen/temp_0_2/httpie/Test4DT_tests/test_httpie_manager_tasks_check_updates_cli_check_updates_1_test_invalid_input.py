
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.check_updates import cli_check_updates, Environment, ExitStatus

class TestCliCheckUpdates(unittest.TestCase):
    @patch('httpie.manager.tasks.check_updates.get_update_status')
    @patch('httpie.manager.tasks.check_updates.fetch_updates')
    def test_invalid_input(self, mock_fetch_updates, mock_get_update_status):
        # Create a mock Environment object
        env = MagicMock()
        
        # Create an invalid argparse.Namespace object with no arguments
        args = unittest.mock.MagicMock()
        
        # Call the function to be tested
        result = cli_check_updates(env, args)
        
        # Assert that fetch_updates and get_update_status were called with the correct parameters
        mock_fetch_updates.assert_called_once_with(env, lazy=False)
        mock_get_update_status.assert_called_once_with(env)
        
        # Assert that the function returns ExitStatus.SUCCESS
        self.assertEqual(result, ExitStatus.SUCCESS)
