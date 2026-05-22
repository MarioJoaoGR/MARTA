
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

def test_valid_inputs():
    with patch('httpie.plugins.manager.PluginManager.get_auth_plugins', return_value=[MagicMock(auth_type='basic'), MagicMock(auth_type='bearer'), MagicMock(auth_type='api_key')]):
        manager = PluginManager()
        plugin_mapping = manager.get_auth_plugin_mapping()
        assert isinstance(plugin_mapping, dict)
        assert len(plugin_mapping) == 3
        for key in ['basic', 'bearer', 'api_key']:
            assert key in plugin_mapping
            assert isinstance(plugin_mapping[key], MagicMock)
