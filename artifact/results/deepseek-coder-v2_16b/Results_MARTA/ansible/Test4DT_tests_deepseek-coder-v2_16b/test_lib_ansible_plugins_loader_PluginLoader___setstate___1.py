
import pytest
from ansible.plugins.loader import PluginLoader

# Test valid inputs
def test_valid_inputs():
    loader = PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], 'plugins')
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config == [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}]
    assert loader.subdir == 'plugins'

# Test edge cases with boundary values and None inputs
def test_edge_cases():
    loader = PluginLoader(None, None, [], None)
    assert loader.class_name is None
    assert loader.package is None
    assert loader.config == []
    assert loader.subdir is None

# Test invalid inputs that should raise exceptions
def test_invalid_inputs():
    with pytest.raises(TypeError):
        PluginLoader()  # Missing arguments
    with pytest.raises(TypeError):
        PluginLoader('MyClass')  # Missing package argument
    with pytest.raises(TypeError):
        PluginLoader('MyClass', 'my_package')  # Missing config argument
    with pytest.raises(TypeError):
        PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}])  # Missing subdir argument
