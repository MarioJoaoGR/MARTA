
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

def test_none_input():
    manager = PluginManager()
    
    with patch('httpie.plugins.manager.PluginManager.__iter__', return_value=[]):
        with pytest.raises(TypeError):
            manager.filter(by_type=None)
