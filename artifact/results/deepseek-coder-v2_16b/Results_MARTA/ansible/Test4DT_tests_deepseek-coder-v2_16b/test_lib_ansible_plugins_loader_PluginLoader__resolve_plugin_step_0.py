
import pytest
from ansible.plugins.loader import PluginLoader



def test_no_config():
    loader = PluginLoader('MyClass', 'my_package', [], 'plugins')
    assert len(loader.config) == 0, "Expected no configurations in the config list"