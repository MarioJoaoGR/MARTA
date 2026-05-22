
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.manager import PluginManager
from typing import List, Type

class FormatterPlugin:
    pass

def test_none_case():
    with patch.object(PluginManager, 'get_formatters', return_value=None):
        manager = PluginManager()
        assert manager.get_formatters() is None
