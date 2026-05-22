
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

def test_edge_cases():
    manager = PluginManager()
    
    # Test when get_auth_plugins returns None
    with patch.object(PluginManager, 'get_auth_plugins', return_value=None):
        with pytest.raises(TypeError):
            manager.get_auth_plugin_mapping()
