
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
        
        # Mocking the json module to return a JSON string
        mock_json.dumps.return_value = '{"mocked": "data"}'
        
        # Mocking the to_data function to return some data
        mock_to_data.return_value = {'mocked': 'data'}
        
        # Call the function under test
        result = cli_export_args(env, args)
        
        # Assertions
        self.assertEqual(result, ExitStatus.SUCCESS)
        mock_json.dumps.assert_called_once_with({'mocked': 'data'})
        mock_to_data.assert_called_once()
        mock_write_raw_data.assert_called_once_with(env, '{"mocked": "data"}', stream_kwargs={'mime_overwrite': FORMAT_TO_CONTENT_TYPE['json']})
