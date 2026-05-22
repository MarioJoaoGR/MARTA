
import unittest.mock as mock
from importlib import metadata as importlib_metadata
from httpie.compat import get_dist_name

def test_invalid_entry_point():
    with mock.patch('httpie.compat.importlib_metadata') as mock_metadata:
        mock_metadata.EntryPoint = mock.Mock()
        entry_point = mock_metadata.EntryPoint.return_value
        entry_point.dist = None
        entry_point.pattern = mock.Mock()
        entry_point.pattern.match.return_value = None
        entry_point.value = 'invalid_module'
        
        result = get_dist_name(entry_point)
        
        assert result is None
