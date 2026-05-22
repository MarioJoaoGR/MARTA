
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from typing import List, Type

class FormatterPlugin:
    pass

def test_get_formatters():
    manager = PluginManager()
    
    # Test when no formatters are registered
    with patch('httpie.plugins.manager.PluginManager.filter', return_value=[]):
        assert manager.get_formatters() == []
    
    # Test when some formatters are registered
    mock_formatter1 = MagicMock(spec=FormatterPlugin)
    mock_formatter2 = MagicMock(spec=FormatterPlugin)
    with patch('httpie.plugins.manager.PluginManager.filter', return_value=[mock_formatter1, mock_formatter2]):
        assert isinstance(manager.get_formatters()[0], FormatterPlugin)
        assert isinstance(manager.get_formatters()[1], FormatterPlugin)
    
    # Test when None is returned
    with patch('httpie.plugins.manager.PluginManager.filter', return_value=None):
        assert manager.get_formatters() is None
    
    # Test when an empty list is returned
    with patch('httpie.plugins.manager.PluginManager.filter', return_value=[]):
        assert manager.get_formatters() == []
