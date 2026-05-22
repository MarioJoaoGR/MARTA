
import pytest
from unittest.mock import patch, MagicMock
import importlib_metadata
from httpie.compat import get_dist_name

def test_none_input():
    with patch('importlib_metadata.EntryPoint') as mock_entry_point:
        mock_entry_point_instance = mock_entry_point.return_value
        mock_entry_point_instance.dist = None
        mock_entry_point_instance.pattern.match.return_value = None
        
        result = get_dist_name(mock_entry_point_instance)
        assert result is None
