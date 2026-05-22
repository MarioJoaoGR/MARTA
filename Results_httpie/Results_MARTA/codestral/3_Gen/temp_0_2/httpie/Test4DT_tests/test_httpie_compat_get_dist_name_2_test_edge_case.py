
import unittest.mock as mock
from httpie.compat import get_dist_name

def test_edge_case():
    with mock.patch('httpie.compat.importlib_metadata') as mock_metadata:
        # Mock an EntryPoint object
        entry_point = mock.Mock()
        entry_point.value = 'some_module'
        
        # Mock the dist attribute of the EntryPoint
        dist = mock.Mock()
        dist.name = 'some_dist_name'
        entry_point.dist = dist
        
        # Mock metadata to return a name
        metadata = mock.Mock()
        metadata.get.return_value = 'some_dist_name'
        mock_metadata.metadata.return_value = metadata
        
        result = get_dist_name(entry_point)
        assert result == 'some_dist_name'
