# Module: ansible.plugins.loader
import pytest
from collections import defaultdict
import sys
import warnings
import imp
import importlib.util

# Define necessary constants or imports if required by the PluginLoader class
MODULE_CACHE = {}
PATH_CACHE = {}
PLUGIN_PATH_CACHE = {}

class PluginLoader:
    def __init__(self, class_name, package, config, subdir, aliases=None, required_base_class=None):
        aliases = {} if aliases is None else aliases
        self.class_name = class_name
        self.base_class = required_base_class
        self.package = package
        self.subdir = subdir
        self.aliases = aliases

        if config and not isinstance(config, list):
            config = [config]
        elif not config:
            config = []

        self.config = config

        if class_name not in MODULE_CACHE:
            MODULE_CACHE[class_name] = {}
        if class_name not in PATH_CACHE:
            PATH_CACHE[class_name] = None
        if class_name not in PLUGIN_PATH_CACHE:
            PLUGIN_PATH_CACHE[class_name] = defaultdict(dict)

        self._extra_dirs = []
        self._module_cache = MODULE_CACHE[class_name]
        self._paths = PATH_CACHE[class_name]
        self._plugin_path_cache = PLUGIN_PATH_CACHE[class_name]
        self._searched_paths = set()

    def _load_module_source(self, name, path):
        if name.startswith('ansible_collections.'):
            full_name = name
        else:
            full_name = '.'.join([self.package, name])

        if full_name in sys.modules:
            return sys.modules[full_name]

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            if imp is None:
                spec = importlib.util.spec_from_file_location(to_native(full_name), to_native(path))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                sys.modules[full_name] = module
            else:
                with open(to_bytes(path), 'rb') as module_file:
                    module = imp.load_source(to_native(full_name), to_native(path), module_file)
        return module

# Test cases for PluginLoader class
def test_pluginloader_init():
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins')
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config == ['/path/to/config']
    assert loader.subdir == 'plugins'
    assert loader.aliases == {}
    assert loader.base_class is None

def test_pluginloader_load_module_source():
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins')
    module = loader._load_module_source('my_plugin_name', '/path/to/plugin.py')
    assert module is not None, "Module should be loaded successfully"

def test_pluginloader_load_module_source_existing():
    # Ensure the module is already in sys.modules to simulate an existing module
    sys.modules['my_package.my_plugin_name'] = object()
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins')
    module = loader._load_module_source('my_plugin_name', '/path/to/plugin.py')
    assert module is sys.modules['my_package.my_plugin_name']

def test_pluginloader_load_module_source_invalid():
    with pytest.raises(Exception):
        loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins')
        module = loader._load_module_source('my_plugin_name', '/nonexistent/path/plugin.py')
