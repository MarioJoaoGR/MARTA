
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from typing import List, Type

class FormatterPlugin:
    pass

def test_valid_inputs():
    with patch('httpie.plugins.manager.PluginManager.filter', autospec=True) as mock_filter:
        manager = PluginManager()
        mock_formatter = MagicMock(spec=FormatterPlugin)
        mock_filter.return_value = [mock_formatter]
        
        formatters = manager.get_formatters()
        
        assert isinstance(formatters, list), "Expected a list of formatter plugins"
        assert all(isinstance(f, FormatterPlugin) for f in formatters), "All items in the list should be instances of FormatterPlugin"
        assert len(formatters) == 1, "Expected exactly one formatter plugin to be returned"
