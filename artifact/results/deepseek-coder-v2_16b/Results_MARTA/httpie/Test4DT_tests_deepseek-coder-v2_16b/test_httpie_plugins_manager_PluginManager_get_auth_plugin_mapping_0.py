
import pytest
from httpie.plugins.manager import PluginManager
from unittest.mock import patch

def test_get_auth_plugin_mapping_empty():
    manager = PluginManager()
    with patch('httpie.plugins.manager.PluginManager.get_auth_plugins', return_value=[]):
        auth_plugin_mapping = manager.get_auth_plugin_mapping()
        assert isinstance(auth_plugin_mapping, dict)
        assert len(auth_plugin_mapping) == 0
