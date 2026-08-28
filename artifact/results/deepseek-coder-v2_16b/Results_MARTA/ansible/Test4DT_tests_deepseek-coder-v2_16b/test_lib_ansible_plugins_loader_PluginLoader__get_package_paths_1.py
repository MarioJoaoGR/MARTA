
import pytest
from ansible.plugins.loader import PluginLoader

# Test scenario 1: Initialize PluginLoader with valid parameters

# Test scenario 2: Initialize PluginLoader without aliases
def test_no_aliases():
    config = [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}]
    loader = PluginLoader('MyClass', 'my_package', config, 'plugins')
    
    assert isinstance(loader.aliases, dict) and not loader.aliases

# Test scenario 3: Initialize PluginLoader with required base class specified

# Test scenario 4: Initialize PluginLoader with empty configuration
def test_empty_config():
    loader = PluginLoader('MyClass', 'my_package', [], 'plugins')
    
    assert loader.config == []