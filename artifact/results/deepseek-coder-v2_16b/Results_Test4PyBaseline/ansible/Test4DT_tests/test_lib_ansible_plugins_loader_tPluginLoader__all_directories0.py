# Module: ansible.plugins.loader
import pytest
from collections import defaultdict
import os

# Assuming MODULE_CACHE, PATH_CACHE, and PLUGIN_PATH_CACHE are defined elsewhere in your code.
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

        # FIXME: remove alias dict in favor of alias by symlink?
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

        # hold dirs added at runtime outside of config
        self._extra_dirs = []

        # caches
        self._module_cache = MODULE_CACHE[class_name]
        self._paths = PATH_CACHE[class_name]
        self._plugin_path_cache = PLUGIN_PATH_CACHE[class_name]

        self._searched_paths = set()

    def _all_directories(self, dir):
        results = []
        results.append(dir)
        for root, subdirs, files in os.walk(dir, followlinks=True):
            if '__init__.py' in files:
                for x in subdirs:
                    results.append(os.path.join(root, x))
        return results

# Test cases for PluginLoader class
def test_pluginloader_initialization():
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins')
    assert loader.class_name == 'MyClass'
    assert loader.package == 'my_package'
    assert loader.config == ['/path/to/config']
    assert loader.subdir == 'plugins'
    assert not loader.aliases
    assert not loader.base_class

def test_pluginloader_with_empty_config():
    loader = PluginLoader('MyClass', 'my_package', [], 'plugins')
    assert loader.config == []

def test_pluginloader_with_single_config():
    loader = PluginLoader('MyClass', 'my_package', '/path/to/config', 'plugins')
    assert loader.config == ['/path/to/config']

def test_all_directories_method():
    loader = PluginLoader('MyClass', 'my_package', ['/path/to/config'], 'plugins')
    dirs = loader._all_directories('/some/directory')
    assert isinstance(dirs, list)
    for dir in dirs:
        assert os.path.isabs(dir)

# Add more test cases as needed to cover different scenarios and edge cases.
