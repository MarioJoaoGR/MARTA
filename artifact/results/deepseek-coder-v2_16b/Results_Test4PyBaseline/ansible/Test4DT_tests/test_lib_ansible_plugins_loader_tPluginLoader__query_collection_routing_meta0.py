
# Module: ansible.plugins.loader
# test_plugin_loader.py
from ansible.plugins.loader import PluginLoader
import pytest
from unittest.mock import patch
from collections import defaultdict
import importlib

@pytest.fixture
def plugin_loader():
    return PluginLoader('MyClass', 'my_package', ['/path/to/config1', '/path/to/config2'], 'plugins')

def test_plugin_loader_init(plugin_loader):
    assert plugin_loader.class_name == 'MyClass'
    assert plugin_loader.package == 'my_package'
    assert plugin_loader.config == ['/path/to/config1', '/path/to/config2']
    assert plugin_loader.subdir == 'plugins'
    assert plugin_loader.aliases == {}