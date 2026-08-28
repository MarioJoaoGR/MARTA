
import pytest
from ansible.plugins.loader import PluginLoader

def test_plugin_loader_initialization():
    minimal_args = ['MyClass', 'my_package', [], 'plugins']
    loader = PluginLoader(*minimal_args)
    
    assert hasattr(loader, 'class_name') and loader.class_name == 'MyClass'
    assert hasattr(loader, 'config') and len(loader.config) == 0
    assert hasattr(loader, 'subdir') and loader.subdir == 'plugins'
