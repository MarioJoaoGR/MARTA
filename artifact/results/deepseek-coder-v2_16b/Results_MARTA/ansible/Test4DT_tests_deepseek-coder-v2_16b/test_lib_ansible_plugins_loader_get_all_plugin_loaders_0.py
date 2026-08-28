
import pytest
from ansible.plugins.loader import PluginLoader

def get_all_plugin_loaders():
    return [(name, obj) for (name, obj) in globals().items() if isinstance(obj, PluginLoader)]

# Test scenarios


def test_edge_cases():
    # Mocking an empty global namespace
    globals_mock = {}
    
    # Replace the globals() with our mock
    with pytest.MonkeyPatch.context():
        import sys
        sys._getframe(0).f_globals.update(globals_mock)
        
        result = get_all_plugin_loaders()
        assert len(result) == 0, "Expected no plugin loaders but got some"

def test_invalid_inputs():
    # Mocking a global namespace with an unexpected structure
    globals_mock = {'invalid': "not a PluginLoader"}
    
    # Replace the globals() with our mock
    with pytest.MonkeyPatch.context():
        import sys
        sys._getframe(0).f_globals.update(globals_mock)
        
        result = get_all_plugin_loaders()
        assert len(result) == 0, "Expected no plugin loaders but got some"