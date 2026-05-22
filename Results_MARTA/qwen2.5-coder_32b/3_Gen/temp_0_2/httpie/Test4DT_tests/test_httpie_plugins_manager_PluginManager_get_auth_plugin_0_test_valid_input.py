
import unittest
from httpie.plugins.manager import PluginManager
from unittest.mock import patch, MagicMock

class TestPluginManager(unittest.TestCase):
    
    @patch('httpie.plugins.manager.PluginManager.get_auth_plugin_mapping')
    def test_valid_input(self, mock_get_auth_plugin_mapping):
        # Create a mock AuthPlugin class
        class MockAuthPlugin:
            pass
        
        # Set up the mock mapping to return the MockAuthPlugin for "exampleType"
        mock_get_auth_plugin_mapping.return_value = {
            "exampleType": MockAuthPlugin
        }
        
        manager = PluginManager()
        auth_plugin = manager.get_auth_plugin("exampleType")
        
        # Assert that the returned class is indeed the MockAuthPlugin
        self.assertIs(auth_plugin, MockAuthPlugin)
