
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.processing import Formatting, Environment, plugin_manager

def test_invalid_input():
    with patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={'default': [MagicMock()]}):
        with pytest.raises(KeyError):
            Formatting(groups=['nonexistent'], env=Environment())
