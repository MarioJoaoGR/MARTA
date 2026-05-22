
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

@pytest.fixture(autouse=True)
def setup_plugin_manager():
    pm = PluginManager()
    yield pm

def test_none_input(setup_plugin_manager):
    with patch('httpie.plugins.manager.PluginManager.iter_entry_points', return_value=[MagicMock()]):
        with patch('httpie.plugins.manager.get_dist_name', return_value='test_plugin'):
            setup_plugin_manager.load_installed_plugins(None)
