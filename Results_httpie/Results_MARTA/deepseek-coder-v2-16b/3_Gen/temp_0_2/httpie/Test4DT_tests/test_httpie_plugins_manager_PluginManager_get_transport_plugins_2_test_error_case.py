
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from typing import List, Type

def test_error_case():
    with patch('httpie.plugins.manager.PluginManager.filter', side_effect=Exception("Test Error")):
        manager = PluginManager()
        with pytest.raises(Exception):
            manager.get_transport_plugins()
