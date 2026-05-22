
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

@pytest.fixture(autouse=True)
def setup_plugin_manager():
    pm = PluginManager()
    yield pm

def test_valid_input(setup_plugin_manager):
    with patch('httpie.plugins.manager.PluginManager.iter_entry_points', return_value=[MagicMock()]):
        valid_dir = Path('/path/to/plugins')
        setup_plugin_manager.load_installed_plugins(valid_dir)
