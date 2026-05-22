
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.processing import Formatting, Environment, plugin_manager

def test_edge_case():
    with patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={'default': [MagicMock(), MagicMock()]}):
        # Test with None for groups
        with pytest.raises(TypeError):
            Formatting(groups=None)
        
        # Test with empty list for groups
        formatting = Formatting(groups=[])
        assert formatting.enabled_plugins == []
