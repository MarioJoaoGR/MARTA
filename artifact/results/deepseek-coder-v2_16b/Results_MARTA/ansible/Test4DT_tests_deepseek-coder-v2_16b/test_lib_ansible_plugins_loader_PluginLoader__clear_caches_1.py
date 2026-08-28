
import pytest
from ansible.plugins.loader import PluginLoader
import os
from collections import defaultdict

# Define constants for testing
C = type('Constants', (), {'OLD_PLUGIN_CACHE_CLEARING': True})()
MODULE_CACHE = {}
PATH_CACHE = {}
PLUGIN_PATH_CACHE = {}

@pytest.fixture(scope="module")
def plugin_loader():
    return PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], 'plugins')

# Test for clearing caches when OLD_PLUGIN_CACHE_CLEARING is True
def test_clear_caches(plugin_loader):
    plugin_loader._clear_caches()
    assert plugin_loader._paths is None
    assert MODULE_CACHE.get('MyClass', {}) == {}
    assert PATH_CACHE.get('MyClass', None) is None
    assert PLUGIN_PATH_CACHE.get('MyClass', defaultdict(dict)) == defaultdict(dict)

# Test for clearing caches when OLD_PLUGIN_CACHE_CLEARING is False
def test_old_cache_clearing(plugin_loader):
    plugin_loader._clear_caches()  # Assuming C.OLD_PLUGIN_CACHE_CLEARING is True for this test
    assert plugin_loader._paths == None
    assert MODULE_CACHE.get('MyClass', {}) == {}
    assert PATH_CACHE.get('MyClass', None) is None
    assert PLUGIN_PATH_CACHE.get('MyClass', defaultdict(dict)) == defaultdict(dict)
