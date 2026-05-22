
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.processing import Formatting, Environment, plugin_manager

def test_edge_case():
    with patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={'group1': [MagicMock(), MagicMock()], 'group2': []}):
        env = Environment()
        formatting = Formatting(groups=['group1'], env=env)
        assert len(formatting.enabled_plugins) == 2

    with patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={'group1': []}):
        env = Environment()
        formatting = Formatting(groups=['group1'], env=env)
        assert len(formatting.enabled_plugins) == 0

    with patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={'group1': [MagicMock(), MagicMock()]}):
        formatting = Formatting(groups=[], env=Environment())
        assert len(formatting.enabled_plugins) == 0

    with patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={}):
        with pytest.raises(KeyError):
            formatting = Formatting(groups=['group1'], env=Environment())
