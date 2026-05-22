
import unittest
from unittest.mock import patch, MagicMock
from httpie.cli.requestitems import KeyValueArg, process_data_embed_raw_json_file_arg

class TestHttpieCliRequestitemsProcessDataEmbedRawJsonFileArg(unittest.TestCase):
    @patch('httpie.cli.requestitems.load_text_file')
    @patch('httpie.cli.requestitems.load_json')
    def test_valid_input(self, mock_load_json, mock_load_text_file):
        # Arrange
        arg = MagicMock()
        arg.value = 'path/to/file'
        expected_json_data = {'key': 'value'}
        
        mock_load_text_file.return_value = '{"key": "value"}'
        mock_load_json.return_value = expected_json_data
        
        # Act
        result = process_data_embed_raw_json_file_arg(arg)
        
        # Assert
        self.assertEqual(result, expected_json_data)
        mock_load_text_file.assert_called_once_with(arg)
        mock_load_json.assert_called_once_with(arg, '{"key": "value"}')
