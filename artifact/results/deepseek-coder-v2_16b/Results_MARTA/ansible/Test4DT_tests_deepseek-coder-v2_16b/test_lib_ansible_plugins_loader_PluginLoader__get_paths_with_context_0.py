
import pytest
from ansible.plugins.loader import PluginLoader

def test_invalid_input():
    config = {'plugin1': '/path/to/config1'}
    loader = PluginLoader('MyClass', 'my_package', config, 'plugins')
    
    with pytest.raises(TypeError):
        loader.get('example_plugin')
