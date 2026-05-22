
from httpie.plugins.manager import PluginManager
import pytest

def test_valid_input():
    plugin_manager = PluginManager()
    assert repr(plugin_manager) == f'<PluginManager {plugin_manager}>'
