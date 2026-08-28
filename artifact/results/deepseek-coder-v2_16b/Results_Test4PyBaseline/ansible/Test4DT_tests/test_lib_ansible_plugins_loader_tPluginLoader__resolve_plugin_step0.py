
import pytest
from ansible.plugins.loader import PluginLoader

# Test cases for the PluginLoader class
def test_plugin_loader_init():
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config1', '/path/to/config2'], 'plugins')
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config == ['/path/to/config1', '/path/to/config2']
    assert loader.subdir == 'plugins'