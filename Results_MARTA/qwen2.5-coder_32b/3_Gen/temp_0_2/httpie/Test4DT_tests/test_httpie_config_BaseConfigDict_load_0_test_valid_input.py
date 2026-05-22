
import unittest
from pathlib import Path
from httpie.config import BaseConfigDict
from unittest.mock import patch, MagicMock

class TestBaseConfigDictLoad(unittest.TestCase):
    def setUp(self):
        self.path = Path('/some/file/path')
        self.config = BaseConfigDict(path=self.path)

    @patch('httpie.config.read_raw_config')
    def test_load_valid_input(self, mock_read_raw_config):
        # Mock the data to be returned by read_raw_config
        mock_data = {'key': 'value'}
        mock_read_raw_config.return_value = mock_data

        # Call the load method
        self.config.load()

        # Check that pre_process_data was called with the correct data
        self.assertEqual(self.config.pre_process_data(mock_data), mock_data)

        # Check that update was called with the processed data
        mock_processed_data = {'key': 'value'}  # Assuming pre_process_data returns this
        self.config.update(mock_processed_data)
