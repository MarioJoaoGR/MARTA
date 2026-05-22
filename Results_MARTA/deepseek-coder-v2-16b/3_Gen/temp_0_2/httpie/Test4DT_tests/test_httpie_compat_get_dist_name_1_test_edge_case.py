
import unittest.mock as mock
from httpie.compat import get_dist_name

def test_get_dist_name():
    with mock.patch('httpie.compat.importlib_metadata') as mock_importlib_metadata:
        # Mock an EntryPoint object
        entry_point = mock.Mock()
        dist = mock.Mock()
        dist.name = 'test_dist'
        entry_point.dist = dist
        
        # Call the function
        result = get_dist_name(entry_point)
        
        # Assertions
        assert result == 'test_dist'
