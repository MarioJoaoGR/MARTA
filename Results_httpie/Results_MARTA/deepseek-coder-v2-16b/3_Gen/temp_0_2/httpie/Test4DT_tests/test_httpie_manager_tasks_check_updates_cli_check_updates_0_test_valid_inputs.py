
import unittest
from unittest.mock import patch
from httpie.manager.tasks.check_updates import cli_check_updates, Environment, ExitStatus

class TestCliCheckUpdates(unittest.TestCase):
    @patch('httpie.manager.tasks.check_updates.fetch_updates')
    @patch('httpie.manager.tasks.check_updates.get_update_status')
    def test_valid_inputs(self, mock_get_update_status, mock_fetch_updates):
        # Mocking the Environment and argparse.Namespace objects
        env = Environment()
        args = unittest.mock.Mock()
        
        # Setting up the return values for the mocks
        mock_fetch_updates.return_value = None
        mock_get_update_status.return_value = "Update status"
        
        # Calling the function under test
        result = cli_check_updates(env, args)
        
        # Asserting that the mocked methods were called with the correct arguments
        mock_fetch_updates.assert_called_once_with(env, lazy=False)
        mock_get_update_status.assert_called_once_with(env)
        
        # Asserting the return value of the function
        self.assertEqual(result, ExitStatus.SUCCESS)
