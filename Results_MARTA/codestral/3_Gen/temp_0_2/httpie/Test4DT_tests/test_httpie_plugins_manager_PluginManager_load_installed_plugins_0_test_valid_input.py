
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

@pytest.fixture(autouse=True)
def setup_plugin_manager():
    pm = PluginManager()
    yield

@pytest.mark.parametrize("valid_dir", [Path("/path/to/plugins")])
def test_valid_input(valid_dir):
    with patch('httpie.plugins.manager.PluginManager.iter_entry_points', return_value=[MagicMock()]):
        pm = PluginManager()
        pm.load_installed_plugins(valid_dir)
