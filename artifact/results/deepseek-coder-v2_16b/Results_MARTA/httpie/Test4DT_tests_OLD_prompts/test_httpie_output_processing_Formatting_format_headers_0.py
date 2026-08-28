
import pytest
from unittest.mock import patch
from httpie.output.processing import Formatting, plugin_manager, Environment

def test_formatting_initialization():
    with patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={'group1': [], 'group2': []}):
        formatter = Formatting(groups=["group1", "group2"])
        assert hasattr(formatter, 'enabled_plugins')

def test_formatting_initialization_with_env_and_kwargs():
    env = Environment()
    with patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={'group1': [], 'group2': []}):
        formatter = Formatting(groups=["group1", "group2"], env=env, custom_arg="custom_value")
        assert hasattr(formatter, 'enabled_plugins')
