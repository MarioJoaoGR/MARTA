
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

def test_none_input():
    manager = PluginManager()
    
    with patch('httpie.plugins.manager.PluginManager.filter', side_effect=TypeError):
        with pytest.raises(TypeError):
            filtered_plugins = manager.filter(by_type=None)
