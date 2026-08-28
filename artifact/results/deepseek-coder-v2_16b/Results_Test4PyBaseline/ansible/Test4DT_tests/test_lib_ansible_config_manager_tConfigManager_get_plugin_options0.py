
# Module: ansible.config.manager
# test_config_manager.py
from ansible.config.manager import ConfigManager
import os

def test_get_plugin_options_basic():
    config_manager = ConfigManager()  # Instantiate the ConfigManager
    plugin_options = config_manager.get_plugin_options('type', 'name')
    assert isinstance(plugin_options, dict), "Expected a dictionary"