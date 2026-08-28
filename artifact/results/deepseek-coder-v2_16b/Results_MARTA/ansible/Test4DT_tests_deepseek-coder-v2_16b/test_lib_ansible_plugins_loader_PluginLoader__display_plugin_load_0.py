
import pytest
from ansible.plugins.loader import PluginLoader

def test_plugin_loader_initialization():
    loader = PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], 'plugins')
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert len(loader.config) == 2
    assert all(isinstance(item, dict) for item in loader.config)
    assert loader.subdir == 'plugins'


def test_plugin_loader_add_directory():
    loader = PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], 'plugins')
    initial_dirs = loader._extra_dirs.copy()
    loader.add_directory('/new/path/to/additional/plugins')
    assert len(loader._extra_dirs) == len(initial_dirs) + 1, "Expected additional directory to be added"
