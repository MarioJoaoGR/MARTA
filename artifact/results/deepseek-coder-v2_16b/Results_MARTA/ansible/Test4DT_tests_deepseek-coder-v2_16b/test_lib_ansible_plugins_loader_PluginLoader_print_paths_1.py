
import pytest
from ansible.plugins.loader import PluginLoader

# Test scenarios
def test_valid_input():
    loader = PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], 'plugins')
    assert isinstance(loader, PluginLoader)
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config == [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}]
    assert loader.subdir == 'plugins'

def test_edge_case():
    loader = PluginLoader('MyClass', 'my_package', None, 'plugins')
    assert isinstance(loader, PluginLoader)
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config is None
    assert loader.subdir == 'plugins'

def test_invalid_input():
    with pytest.raises(TypeError):
        PluginLoader('MyClass', 'my_package', ['invalid'], 'plugins')
