
import pytest
from httpie.plugins.manager import PluginManager
from unittest.mock import patch, MagicMock
from typing import Dict, Type


def test_get_auth_plugin_mapping_empty():
    manager = PluginManager()
    
    # Mocking the get_auth_plugins method to return an empty list
    with patch.object(PluginManager, 'get_auth_plugins', return_value=[]):
        result = manager.get_auth_plugin_mapping()
        
        # Assert that the result is a dictionary
        assert isinstance(result, dict)
        # Assert that the dictionary is empty
        assert len(result) == 0
