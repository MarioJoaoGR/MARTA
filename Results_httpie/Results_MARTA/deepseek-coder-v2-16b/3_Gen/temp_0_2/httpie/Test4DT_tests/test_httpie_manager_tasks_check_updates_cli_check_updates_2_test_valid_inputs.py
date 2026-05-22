
import unittest
from unittest.mock import patch
from httpie.manager.tasks.check_updates import cli_check_updates, Environment, ExitStatus

class TestCliCheckUpdates(unittest.TestCase):
    @patch('httpie.manager.tasks.check_updates.fetch_updates')
    @patch('httpie.manager.tasks.check_updates.get_update_status')
    def test_valid_inputs(self, mock_get_update_status, mock_fetch_updates):
        # Mocking the environment and arguments for the function call
        env = Environment()
        args = unittest.mock.Mock()
        
        # Setting up the expected behavior of mocked functions
        mock_fetch_updates.return_value = None  # Assuming fetch_updates returns nothing
        mock_get_update_status.return_value = "Update status: Available"  # Example update status
        
        # Calling the function under test
        result = cli_check_updates(env, args)
        
        # Assertions to verify the expected outcomes
        self.assertEqual(result, ExitStatus.SUCCESS)
        mock_fetch_updates.assert_called_once_with(env, lazy=False)
        mock_get_update_status.assert_called_once_with(env)
