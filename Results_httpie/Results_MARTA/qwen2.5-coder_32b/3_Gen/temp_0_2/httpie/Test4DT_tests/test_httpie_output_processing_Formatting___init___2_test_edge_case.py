
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.processing import Formatting, Environment, plugin_manager

def test_edge_case():
    with patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={'html': [MagicMock()], 'csv': [MagicMock()]}):
        env = Environment()
        formatting = Formatting(groups=['html', 'csv'], env=env)
        
        assert len(formatting.enabled_plugins) == 2
