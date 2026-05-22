
import unittest
from unittest.mock import patch
from httpie.plugins.manager import PluginManager, AuthPlugin

class TestPluginManagerGetAuthPlugin(unittest.TestCase):
    @patch('httpie.plugins.manager.PluginManager.get_auth_plugin_mapping')
    def test_valid_input(self, mock_get_auth_plugin_mapping):
        # Mock the return value of get_auth_plugin_mapping()
        mock_get_auth_plugin_mapping.return_value = {
            "exampleType": AuthPlugin
        }
        
        manager = PluginManager()
        auth_plugin = manager.get_auth_plugin("exampleType")
        
        # Assert that the returned type is correct
        self.assertIs(auth_plugin, AuthPlugin)
