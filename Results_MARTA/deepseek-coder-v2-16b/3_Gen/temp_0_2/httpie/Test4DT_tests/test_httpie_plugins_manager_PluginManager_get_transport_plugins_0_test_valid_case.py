
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from typing import List, Type

class TransportPlugin:
    pass

def test_valid_case():
    with patch('httpie.plugins.manager.PluginManager') as MockPluginManager:
        mock_instance = MockPluginManager.return_value
        mock_instance.get_transport_plugins.return_value = [MagicMock(spec=TransportPlugin)]
        
        manager = PluginManager()
        transport_plugins: List[Type[TransportPlugin]] = manager.get_transport_plugins()
        
        assert isinstance(transport_plugins, list)
        assert all(isinstance(plugin, TransportPlugin) for plugin in transport_plugins)
