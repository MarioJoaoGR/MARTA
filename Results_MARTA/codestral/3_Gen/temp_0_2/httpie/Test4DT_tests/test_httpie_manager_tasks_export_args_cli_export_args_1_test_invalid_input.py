
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.export_args import cli_export_args, Environment, ExitStatus, argparse

class TestCliExportArgs(unittest.TestCase):
    @patch('httpie.manager.tasks.export_args.write_raw_data')
    @patch('httpie.manager.tasks.export_args.json')
    def test_invalid_input(self, mock_json, mock_write_raw_data):
        # Create a mock environment and arguments with an invalid format
        env = Environment()
        args = argparse.Namespace(format='invalid_format')
        
        # Call the function under test
        with self.assertRaises(NotImplementedError) as context:
            cli_export_args(env, args)
        
        # Check that the error message is correct
        self.assertEqual(str(context.exception), "Unexpected format value: invalid_format")
        
        # Ensure write_raw_data was not called
        mock_write_raw_data.assert_not_called()
        # Ensure json.dumps was not called
        mock_json.dumps.assert_not_called()
