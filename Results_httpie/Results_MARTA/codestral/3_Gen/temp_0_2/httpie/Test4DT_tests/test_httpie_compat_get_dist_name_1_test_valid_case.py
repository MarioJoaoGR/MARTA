
import unittest
from unittest.mock import patch, MagicMock
from httpie.compat import get_dist_name
import importlib.metadata as importlib_metadata

class TestGetDistName(unittest.TestCase):
    @patch('httpie.compat.importlib_metadata')
    def test_valid_case(self, mock_importlib_metadata):
        # Mocking the EntryPoint object
        entry_point = MagicMock()
        entry_point.dist = MagicMock()
        entry_point.dist.name = 'some_name'
        
        # Mocking the metadata method to return a metadata object with name attribute
        mock_metadata = MagicMock()
        mock_metadata.get.return_value = 'some_name'
        mock_importlib_metadata.metadata.return_value = mock_metadata
        
        result = get_dist_name(entry_point)
        self.assertEqual(result, 'some_name')
