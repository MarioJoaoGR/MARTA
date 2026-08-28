
import pytest
from ansible.plugins.loader import PluginLoader

# Test Scenario 1: Valid Inputs
def test_valid_inputs():
    loader = PluginLoader(class_name='MyClass', package='my_package', config=[{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], subdir='plugins')
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config == [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}]
    assert loader.subdir == 'plugins'
    assert len(loader.config) == 2

# Test Scenario 2: Edge Cases
def test_edge_cases():
    loader = PluginLoader(class_name=None, package='my_package', config=[], subdir='plugins')
    assert loader.class_name is None
    assert loader.package == 'my_package'
    assert loader.config == []
    assert loader.subdir == 'plugins'

# Test Scenario 3: Invalid Inputs and Error Handling
def test_invalid_inputs():
    with pytest.raises(TypeError):
        PluginLoader()
