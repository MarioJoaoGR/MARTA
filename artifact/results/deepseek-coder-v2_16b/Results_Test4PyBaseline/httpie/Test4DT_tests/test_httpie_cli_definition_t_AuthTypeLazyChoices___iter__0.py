
# Module: httpie.cli.definition
import pytest
from unittest.mock import MagicMock

# Mocking Plugin Manager for testing purposes
class PluginManager:
    def get_auth_plugin_mapping(self):
        return {'1': 'PluginOne', '2': 'PluginTwo', '3': 'PluginThree'}

plugin_manager = PluginManager()

@pytest.fixture
def auth_types():
    # Create an instance of _AuthTypeLazyChoices with the mocked plugin manager
    class _AuthTypeLazyChoices:
        def __contains__(self, item):
            return item in plugin_manager.get_auth_plugin_mapping()
        
        def __iter__(self):
            return iter(sorted(plugin_manager.get_auth_plugin_mapping().keys()))
    return _AuthTypeLazyChoices()

def test_contains_existing_item(auth_types):
    assert '1' in auth_types  # Assuming there's a plugin for '1' as an auth type, this should return True
    assert '2' in auth_types  # Assuming there's a plugin for '2', this should return True

def test_contains_non_existing_item(auth_types):
    assert 'some_other_type' not in auth_types  # Assuming no plugin is registered for this type, returns False

def test_iteration(auth_types):
    expected_auth_types = sorted(['1', '2', '3'])
    actual_auth_types = [auth_type for auth_type in auth_types]
    assert actual_auth_types == expected_auth_types  # This will check if the iteration yields the correct, sorted list of authentication types.
