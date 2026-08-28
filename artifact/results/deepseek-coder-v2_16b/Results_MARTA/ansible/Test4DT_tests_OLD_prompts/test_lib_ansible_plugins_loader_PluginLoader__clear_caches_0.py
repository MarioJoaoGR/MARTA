
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.loader import MODULE_CACHE, PATH_CACHE, PLUGIN_PATH_CACHE
from collections import defaultdict

@pytest.fixture(autouse=True)
def clear_caches():
    with patch('ansible.plugins.loader.MODULE_CACHE', {'MyClass': {}}), \
         patch('ansible.plugins.loader.PATH_CACHE', {'MyClass': None}), \
         patch('ansible.plugins.loader.PLUGIN_PATH_CACHE', {'MyClass': defaultdict(dict)}):
        yield

def test_clear_caches():
    from lib.ansible.plugins.loader import PluginLoader

    loader = PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], 'plugins')
    
    # Call the method to clear caches
    loader._clear_caches()

    # Check if the caches are cleared
    assert MODULE_CACHE['MyClass'] == {}
    assert PATH_CACHE['MyClass'] is None
    assert isinstance(PLUGIN_PATH_CACHE['MyClass'], defaultdict)
