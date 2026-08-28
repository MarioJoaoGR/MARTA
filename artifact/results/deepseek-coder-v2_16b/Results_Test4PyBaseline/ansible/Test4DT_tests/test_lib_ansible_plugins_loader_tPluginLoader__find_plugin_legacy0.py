
# Module: ansible.plugins.loader
# test_plugin_loader.py
from ansible.plugins.loader import PluginLoader
import os

def test_plugin_loader_init():
    # Test initialization of PluginLoader with valid parameters
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config1', '/path/to/config2'], 'plugins')
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config == ['/path/to/config1', '/path/to/config2']
    assert loader.subdir == 'plugins'
    assert isinstance(loader.aliases, dict) and not loader.aliases