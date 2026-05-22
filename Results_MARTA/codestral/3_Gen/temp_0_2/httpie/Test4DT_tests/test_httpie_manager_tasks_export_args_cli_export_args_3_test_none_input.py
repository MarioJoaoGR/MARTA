
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.export_args import cli_export_args, Environment, ExitStatus, json, to_data, write_raw_data, FORMAT_TO_CONTENT_TYPE

class TestCliExportArgs(unittest.TestCase):
    @patch('httpie.manager.tasks.export_args.json')
    @patch('httpie.manager.tasks.export_args.to_data')
    @patch('httpie.manager.tasks.export_args.write_raw_data')
    def test_none_input(self, mock_write_raw_data, mock_to_data, mock_json):
        # Mock data for testing
        env = MagicMock()
        args = MagicMock()
        args.format = 'json'
        
        # Expected output data
        expected_data = b'{"key": "value"}'
        
        # Mocking the to_data function to return a mock dictionary
        mock_to_data.return_value = {'key': 'value'}
        
        # Mocking the json.dumps method to return the expected data
        mock_json.dumps.return_value = expected_data
        
        # Calling the function under test
        result = cli_export_args(env, args)
        
        # Assertions
        self.assertEqual(result, ExitStatus.SUCCESS)
        mock_to_data.assert_called_once()
        mock_json.dumps.assert_called_once_with({'key': 'value'})
        mock_write_raw_data.assert_called_once_with(env, expected_data, stream_kwargs={'mime_overwrite': FORMAT_TO_CONTENT_TYPE['json']})

if __name__ == '__main__':
    unittest.main()
