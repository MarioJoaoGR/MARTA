
import pytest
from ansible.plugins.loader import PluginLoader

# Test cases for PluginLoader class
def test_plugin_loader_basic():
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins')
    assert isinstance(loader, PluginLoader), "PluginLoader instance should be created successfully"

def test_plugin_loader_with_aliases():
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins', aliases={'alias1': '/path/to/alias1'})