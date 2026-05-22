
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from typing import List, Dict, Type
from itertools import groupby
from operator import attrgetter

class FormatterPlugin:
    def __init__(self, group_name):
        self.group_name = group_name

def test_valid_inputs():
    with patch('httpie.plugins.manager.PluginManager.get_formatters', return_value=[FormatterPlugin("html"), FormatterPlugin("csv")]):
        manager = PluginManager()
        grouped_formatters = manager.get_formatters_grouped()
        
        assert isinstance(grouped_formatters, dict)
        for group in grouped_formatters.values():
            assert all(isinstance(f, FormatterPlugin) for f in group)
        assert set(grouped_formatters.keys()) == {'html', 'csv'}
