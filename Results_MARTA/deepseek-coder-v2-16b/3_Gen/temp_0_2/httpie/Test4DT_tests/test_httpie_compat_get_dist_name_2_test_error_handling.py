
import unittest.mock as mock
from httpie.compat import get_dist_name
from importlib import metadata as importlib_metadata
from typing import Optional

def test_error_handling():
    with mock.patch('httpie.compat.importlib_metadata') as mock_metadata:
        # Mock the EntryPoint object
        entry_point = mock.Mock()
        entry_point.dist = None
        entry_point.pattern = mock.Mock()
        entry_point.pattern.match.return_value = None
        entry_point.value = 'some_module'
        
        # Mock the metadata method to raise PackageNotFoundError
        mock_metadata.metadata.side_effect = importlib_metadata.PackageNotFoundError("Mocked error")
        
        result = get_dist_name(entry_point)
        
        assert result is None, f"Expected None, but got {result}"
