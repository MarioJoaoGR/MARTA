
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

@pytest.fixture(autouse=True)
def setup_plugin_manager():
    with patch('httpie.plugins.manager.PluginManager') as MockPluginManager:
        mock_pm = MockPluginManager.return_value
        yield mock_pm

def test_valid_input(setup_plugin_manager):
    valid_dir = Path('/path/to/plugins')
    setup_plugin_manager.load_installed_plugins(valid_dir)
