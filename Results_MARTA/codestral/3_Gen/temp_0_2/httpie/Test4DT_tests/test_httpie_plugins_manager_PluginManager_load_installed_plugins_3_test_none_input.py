
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

def test_none_input():
    pm = PluginManager()
    with patch('httpie.plugins.manager.PluginManager.iter_entry_points', return_value=[]):
        assert pm.load_installed_plugins(None) is None
