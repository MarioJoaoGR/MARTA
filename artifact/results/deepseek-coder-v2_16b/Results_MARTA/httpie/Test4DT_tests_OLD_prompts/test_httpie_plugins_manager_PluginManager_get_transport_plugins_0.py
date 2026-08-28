
import pytest
from httpie.plugins.manager import PluginManager
from typing import List, Type
from unittest.mock import patch

# Test scenario 1: Retrieving transport plugins without any registered plugins
def test_get_transport_plugins_no_registered_plugins():
    manager = PluginManager()
    
    with patch('httpie.plugins.manager.PluginManager.filter', return_value=[]):
        assert manager.get_transport_plugins() == []

# Test scenario 2: Retrieving transport plugins with registered plugins