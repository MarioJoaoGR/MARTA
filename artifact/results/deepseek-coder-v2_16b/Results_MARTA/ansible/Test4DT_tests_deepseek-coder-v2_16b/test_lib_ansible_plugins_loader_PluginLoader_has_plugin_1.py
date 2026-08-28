
import pytest
from ansible.plugins.loader import PluginLoader
import os

@pytest.fixture(scope="module")
def loader():
    return PluginLoader('MyClass', 'my_package', [{'plugin1': '/path/to/config1'}, {'plugin2': '/path/to/config2'}], 'plugins')




def test_has_non_existing_plugin(loader):
    assert not loader.has_plugin('nonexistent_plugin'), "Expected to find no plugin for nonexistent_plugin"