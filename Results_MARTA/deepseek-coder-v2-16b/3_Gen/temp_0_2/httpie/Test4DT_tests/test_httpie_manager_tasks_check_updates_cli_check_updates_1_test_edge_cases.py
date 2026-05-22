
import unittest
from unittest.mock import patch
from httpie.manager.tasks.check_updates import cli_check_updates, Environment, argparse, ExitStatus

class TestCliCheckUpdates(unittest.TestCase):
    @patch('httpie.manager.tasks.check_updates.fetch_updates')
    @patch('httpie.manager.tasks.check_updates.get_update_status')
    def test_cli_check_updates(self, mock_get_update_status, mock_fetch_updates):
        # Mocking the Environment and argparse.Namespace objects
        env = Environment()
        args = argparse.Namespace()
        
        # Setting up the expected behavior of fetch_updates and get_update_status
        mock_fetch_updates.return_value = None  # Assuming fetch_updates returns nothing
        mock_get_update_status.return_value = "Update available"  # Example status
        
        # Calling the function under test
        result = cli_check_updates(env, args)
        
        # Assertions to verify the expected behavior
        self.assertEqual(result, ExitStatus.SUCCESS)
        mock_fetch_updates.assert_called_once_with(env, lazy=False)
        mock_get_update_status.assert_called_once_with(env)
