
# Module: ansible.plugins.loader
import pytest
from ansible.plugins.loader import PluginLoader
import os
from collections import defaultdict

# Mocking the necessary modules and constants for testing
MODULE_CACHE = {}
PATH_CACHE = {}
PLUGIN_PATH_CACHE = {}

@pytest.fixture(autouse=True)
def setup_plugin_loader():
    MODULE_CACHE['MyClass'] = {}
    PATH_CACHE['MyClass'] = None
    PLUGIN_PATH_CACHE['MyClass'] = defaultdict(dict)

class TestPluginLoader:
    
    def test_init_without_aliases_and_required_base_class(self):
        config = [
            {'path': '/path/to/plugin1', 'subdir': 'plugins'},
            {'path': '/path/to/plugin2', 'subdir': 'extensions'}
        ]
        loader = PluginLoader('MyClass', 'my_package', config, 'plugins')
        
        assert loader.class_name == 'MyClass'
        assert loader.base_class is None
        assert loader.package == 'my_package'
        assert loader.subdir == 'plugins'
        assert loader.aliases == {}
        assert isinstance(loader.config, list)
        assert len(loader.config) == 2
    
    def test_init_with_aliases(self):
        aliases = {
            'alias1': '/path/to/alias1',
            'alias2': '/path/to/alias2'
        }
        config = [
            {'path': '/path/to/plugin1', 'subdir': 'plugins'},
            {'path': '/path/to/plugin2', 'subdir': 'extensions'}
        ]
        loader = PluginLoader('MyClass', 'my_package', config, 'plugins', aliases=aliases)
        
        assert loader.class_name == 'MyClass'
        assert loader.base_class is None
        assert loader.package == 'my_package'
        assert loader.subdir == 'plugins'
        assert loader.aliases == aliases
        assert isinstance(loader.config, list)
        assert len(loader.config) == 2
    
    def test_init_with_required_base_class(self):
        config = [
            {'path': '/path/to/plugin1', 'subdir': 'plugins'},
            {'path': '/path/to/plugin2', 'subdir': 'extensions'}
        ]
        loader = PluginLoader('MyClass', 'my_package', config, 'plugins', required_base_class='BaseClass')
        
        assert loader.class_name == 'MyClass'
        assert loader.base_class == 'BaseClass'
        assert loader.package == 'my_package'
        assert loader.subdir == 'plugins'
        assert loader.aliases == {}
        assert isinstance(loader.config, list)
        assert len(loader.config) == 2
    
    def test_format_paths(self):
        paths = ['/path/to/plugin1', '/path/to/plugin2']
        loader = PluginLoader('MyClass', 'my_package', [], 'plugins')
        
        formatted_paths = loader.format_paths(paths)
        assert formatted_paths == os.pathsep.join(['/path/to/plugin1', '/path/to/plugin2'])
