
import pytest
from unittest.mock import patch
from httpie.plugins.manager import PluginManager

def test_plugin_manager_repr():
    with patch('httpie.plugins.manager.PluginManager.__init__', return_value=None):
        plugin_manager = PluginManager()
        assert repr(plugin_manager) == f'<{type(plugin_manager).__name__} {plugin_manager}>'
