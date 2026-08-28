
import pytest
from ansible.plugins.loader import PluginLoader

def test_plugin_loader_initialization():
    loader = PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}], 'plugins')
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config == [{'plugin1': '/path/to/config1'}]
    assert loader.subdir == 'plugins'


def test_plugin_loader_with_aliases():
    loader = PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}], 'plugins', aliases={'AliasName': '/path/to/alias'})
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config == [{'plugin1': '/path/to/config1'}]
    assert loader.subdir == 'plugins'
    assert loader.aliases == {'AliasName': '/path/to/alias'}
