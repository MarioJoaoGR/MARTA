
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from typing import List, Dict, Type
from itertools import groupby
from operator import attrgetter

class FormatterPlugin:
    def __init__(self, group_name):
        self.group_name = group_name

@pytest.fixture(autouse=True)
def setup_plugin_manager():
    with patch('httpie.plugins.manager.PluginManager.get_formatters', return_value=[FormatterPlugin("html"), FormatterPlugin("csv")]):
        manager = PluginManager()
        yield manager

def test_valid_inputs(setup_plugin_manager):
    grouped_formatters = setup_plugin_manager.get_formatters_grouped()
    assert isinstance(grouped_formatters, dict)
    assert len(grouped_formatters) == 2
    for group in grouped_formatters.values():
        assert all(isinstance(f, FormatterPlugin) for f in group)
