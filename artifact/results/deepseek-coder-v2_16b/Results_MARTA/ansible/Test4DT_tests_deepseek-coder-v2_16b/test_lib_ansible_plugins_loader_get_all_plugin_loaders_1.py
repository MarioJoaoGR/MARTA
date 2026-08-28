
import pytest
from ansible.plugins.loader import PluginLoader

def get_all_plugin_loaders():
    return [(name, obj) for (name, obj) in globals().items() if isinstance(obj, PluginLoader)]

# Test function to check valid inputs

# Test function to check missing plugin loaders
def test_missing_plugin_loaders():
    # Clear all variables from the global namespace and ensure no PluginLoader instances are present
    for name in list(globals().keys()):
        if isinstance(globals()[name], PluginLoader):
            del globals()[name]
    
    plugin_loaders = get_all_plugin_loaders()
    assert len(plugin_loaders) == 0

# Test function to check invalid input
def test_invalid_input():
    # Set a variable in the global namespace to an invalid type and ensure it's not recognized as PluginLoader
    globals()['invalid_var'] = "not a PluginLoader"
    
    plugin_loaders = get_all_plugin_loaders()
    assert len(plugin_loaders) == 0