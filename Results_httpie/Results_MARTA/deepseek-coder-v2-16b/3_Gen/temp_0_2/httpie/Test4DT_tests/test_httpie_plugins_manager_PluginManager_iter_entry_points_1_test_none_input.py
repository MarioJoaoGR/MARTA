
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

def test_none_input():
    pm = PluginManager()
    with patch('httpie.plugins.manager.enable_plugins') as mock_enable_plugins:
        mock_enable_plugins.return_value.__enter__.return_value = MagicMock()
        dir_path = None
        result = list(pm.iter_entry_points(dir_path))
        assert len(result) == 0, "Expected no entry points when directory is None"
