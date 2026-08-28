
import pytest
from ansible.plugins.loader import PluginLoader

# Test valid case
def test_valid_case():
    config = [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}]
    loader = PluginLoader('MyClass', 'my_package', config, 'plugins')
    
    assert isinstance(loader, PluginLoader)
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert len(loader.config) == 2
    assert '/path/to/config1' in [entry['plugin1'] for entry in loader.config]
    assert '/path/to/config2' in [entry['plugin2'] for entry in loader.config]
    assert loader.subdir == 'plugins'

# Test edge case with None values
def test_edge_case():
    loader = PluginLoader('MyClass', 'my_package', None, 'plugins')
    
    assert isinstance(loader, PluginLoader)
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config is []
    assert loader.subdir == 'plugins'

# Test error handling with missing plugin resolution
def test_error_handling():
    config = [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}]
    loader = PluginLoader('MyClass', 'my_package', config, 'plugins')
    
    with pytest.raises(ValueError):
        loader._resolve_plugin_step('example_plugin')
