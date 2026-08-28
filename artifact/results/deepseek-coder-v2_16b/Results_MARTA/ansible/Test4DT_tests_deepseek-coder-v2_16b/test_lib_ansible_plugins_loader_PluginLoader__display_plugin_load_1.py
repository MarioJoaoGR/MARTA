
import pytest
from ansible.plugins.loader import PluginLoader

# Test valid case scenario
def test_valid_case():
    loader = PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], 'plugins')
    assert hasattr(loader, 'class_name')
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert len(loader.config) == 2
    assert isinstance(loader.config[0], dict)
    assert isinstance(loader.config[1], dict)
    assert loader.subdir == 'plugins'

# Test edge case scenario with None input
def test_edge_case():
    loader = PluginLoader('MyClass', 'my_package', None, 'plugins')
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config is None
    assert loader.subdir == 'plugins'

# Test invalid input scenario with invalid arguments
def test_invalid_input():
    with pytest.raises(TypeError):
        PluginLoader('MyClass', 'my_package', 'invalid_arg', 'plugins')
