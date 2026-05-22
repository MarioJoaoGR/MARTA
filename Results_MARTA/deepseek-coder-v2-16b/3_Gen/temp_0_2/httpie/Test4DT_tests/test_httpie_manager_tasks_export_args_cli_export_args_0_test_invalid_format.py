
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.export_args import cli_export_args, Environment, ExitStatus, json, to_data, write_raw_data, FORMAT_TO_CONTENT_TYPE

class TestCliExportArgs(unittest.TestCase):
    @patch('httpie.manager.tasks.export_args.json')
    @patch('httpie.manager.tasks.export_args.to_data')
    @patch('httpie.manager.tasks.export_args.write_raw_data')
    def test_invalid_format(self, mock_write_raw_data, mock_to_data, mock_json):
        env = MagicMock()
        args = MagicMock()
        args.format = 'invalid_format'
        
        with self.assertRaises(NotImplementedError) as context:
            cli_export_args(env, args)
        
        self.assertTrue('Unexpected format value:' in str(context.exception))
