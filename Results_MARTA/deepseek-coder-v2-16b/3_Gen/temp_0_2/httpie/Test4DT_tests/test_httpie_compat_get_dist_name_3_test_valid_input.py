
import unittest
from unittest.mock import patch, MagicMock
from httpie.compat import get_dist_name
import importlib_metadata

class TestGetDistName(unittest.TestCase):
    @patch('httpie.compat.importlib_metadata')
    def test_valid_input(self, mock_importlib_metadata):
        # Mock an EntryPoint object with a dist attribute
        entry_point = MagicMock()
        dist = MagicMock()
        dist.name = 'some_dist_name'
        entry_point.dist = dist
        
        # Call the function and assert the result
        self.assertEqual(get_dist_name(entry_point), 'some_dist_name')
        
        # Test when there is no dist attribute
        entry_point.dist = None
        mock_importlib_metadata.PackageNotFoundError = importlib_metadata.PackageNotFoundError
        mock_importlib_metadata.metadata.side_effect = importlib_metadata.PackageNotFoundError('Mocked error')
        
        # Call the function and assert the result when an exception is raised
        self.assertIsNone(get_dist_name(entry_point))
