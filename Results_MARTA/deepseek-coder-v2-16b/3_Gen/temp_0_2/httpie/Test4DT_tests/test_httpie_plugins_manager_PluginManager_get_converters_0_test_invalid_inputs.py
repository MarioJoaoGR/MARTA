
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager

def test_invalid_inputs():
    manager = PluginManager()
    
    with patch('httpie.plugins.manager.PluginManager.filter', side_effect=TypeError):
        with pytest.raises(TypeError):
            manager.get_converters()
