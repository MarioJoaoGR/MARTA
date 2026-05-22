
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from typing import Dict, List, Type
from itertools import groupby
from operator import attrgetter

class FormatterPlugin:
    def __init__(self, group_name):
        self.group_name = group_name

def test_invalid_inputs():
    with patch('httpie.plugins.manager.PluginManager.get_formatters', side_effect=Exception("Mocked Exception")):
        manager = PluginManager()
        with pytest.raises(Exception):
            manager.get_formatters_grouped()
