
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

def test_invalid_input():
    manager = PluginManager()
    
    with patch('httpie.plugins.manager.PluginManager.get_auth_plugin_mapping', return_value={}):
        with pytest.raises(KeyError):
            manager.get_auth_plugin(auth_type="invalidType")
