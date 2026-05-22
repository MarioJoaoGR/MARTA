
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from typing import Type, List

class AuthPlugin:
    pass

def test_edge_cases():
    with patch('httpie.plugins.manager.PluginManager.filter', return_value=[]):
        manager = PluginManager()
        auth_plugins = manager.get_auth_plugins()
        assert auth_plugins == []
