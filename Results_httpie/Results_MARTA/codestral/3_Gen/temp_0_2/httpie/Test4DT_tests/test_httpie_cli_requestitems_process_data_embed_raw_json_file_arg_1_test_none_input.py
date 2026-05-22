
import unittest
from unittest.mock import patch, MagicMock
from httpie.cli.requestitems import process_data_embed_raw_json_file_arg, KeyValueArg

class TestHttpieCliRequestitemsProcessDataEmbedRawJsonFileArg(unittest.TestCase):
    @patch('httpie.cli.requestitems.load_text_file')
    @patch('httpie.cli.requestitems.load_json')
    def test_none_input(self, mock_load_json, mock_load_text_file):
        # Arrange
        arg = KeyValueArg(key=None, value='test_value', sep=None, orig='test_orig')
        mock_load_text_file.return_value = '{"key": "value"}'
        mock_load_json.return_value = {"key": "value"}

        # Act
        result = process_data_embed_raw_json_file_arg(arg)

        # Assert
        self.assertEqual(result, {"key": "value"})
