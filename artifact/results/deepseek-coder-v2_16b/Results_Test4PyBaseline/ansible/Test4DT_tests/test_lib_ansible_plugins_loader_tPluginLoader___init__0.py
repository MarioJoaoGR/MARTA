
# Module: ansible.plugins.loader
import pytest
from ansible.plugins.loader import PluginLoader

# Test Case 1: Basic Usage
def test_basic_usage():
    loader = PluginLoader('MyClass', 'my_package', [], 'plugins')
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config == []
    assert loader.subdir == 'plugins'
    assert not loader.aliases
    assert not loader.base_class

# Test Case 2: With Aliases
def test_with_aliases():
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins', aliases={'alias1': '/path/to/alias1'})
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config == ['/path/to/config']
    assert loader.subdir == 'plugins'
    assert loader.aliases == {'alias1': '/path/to/alias1'}
    assert not loader.base_class

# Test Case 3: With Required Base Class
def test_with_required_base_class():
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins', required_base_class='BaseClass')
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config == ['/path/to/config']
    assert loader.subdir == 'plugins'
    assert not loader.aliases
    assert loader.base_class == 'BaseClass'

# Test Case 4: Full Configuration
def test_full_configuration():
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config1', '/path/to/config2'], 'plugins', aliases={'alias1': '/path/to/alias1'}, required_base_class='BaseClass')
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config == ['/path/to/config1', '/path/to/config2']
    assert loader.subdir == 'plugins'
    assert loader.aliases == {'alias1': '/path/to/alias1'}
    assert loader.base_class == 'BaseClass'
