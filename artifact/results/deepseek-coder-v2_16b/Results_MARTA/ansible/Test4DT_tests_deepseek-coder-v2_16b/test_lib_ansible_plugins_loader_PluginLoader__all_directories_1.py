
import pytest
from ansible.plugins.loader import PluginLoader
import os

@pytest.fixture(scope="module")
def plugin_loader():
    return PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], 'plugins')

def test_invalid_input(plugin_loader):
    with pytest.raises(TypeError):
        plugin_loader('invalid')
