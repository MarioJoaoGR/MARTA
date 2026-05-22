
import unittest
from unittest.mock import patch
from httpie.manager.tasks.check_updates import cli_check_updates, Environment, ExitStatus

class TestCliCheckUpdates(unittest.TestCase):
    @patch('httpie.manager.tasks.check_updates.fetch_updates')
    @patch('httpie.manager.tasks.check_updates.get_update_status')
    def test_valid_input(self, mock_get_update_status, mock_fetch_updates):
        # Mocking the Environment instance and argparse.Namespace object
        env = Environment()
        args = unittest.mock.Mock()
        
        # Setting up return values for mocked functions
        mock_fetch_updates.return_value = None  # Assuming fetch_updates does not return anything
        mock_get_update_status.return_value = "Updated"  # Mocking the status output
        
        # Calling the function under test
        result = cli_check_updates(env, args)
        
        # Assertions to verify the mocked functions were called correctly
        mock_fetch_updates.assert_called_once_with(env, lazy=False)
        mock_get_update_status.assert_called_once_with(env)
        
        # Asserting that the function returns the expected ExitStatus
        self.assertEqual(result, ExitStatus.SUCCESS)
