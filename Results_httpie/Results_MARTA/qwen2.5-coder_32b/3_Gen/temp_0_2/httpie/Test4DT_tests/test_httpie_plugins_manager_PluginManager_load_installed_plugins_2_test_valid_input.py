
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

@pytest.fixture(autouse=True)
def setup_plugin_manager():
    pm = PluginManager()
    yield

def test_valid_input():
    with patch('httpie.plugins.manager.PluginManager.iter_entry_points', return_value=[MagicMock()]):
        dir_path = '/valid/directory'
        pm = PluginManager()
        pm.load_installed_plugins(Path(dir_path))
