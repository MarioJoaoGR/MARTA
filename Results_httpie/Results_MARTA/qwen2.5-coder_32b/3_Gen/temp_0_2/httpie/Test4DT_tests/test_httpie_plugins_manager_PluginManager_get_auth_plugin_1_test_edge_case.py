
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

def test_edge_case():
    manager = PluginManager()
    
    # Test with None input
    with pytest.raises(KeyError):
        manager.get_auth_plugin(auth_type=None)
    
    # Test with empty string input
    with pytest.raises(KeyError):
        manager.get_auth_plugin(auth_type="")
