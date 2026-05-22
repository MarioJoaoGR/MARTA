
import unittest
from unittest.mock import patch
from httpie.plugins.manager import PluginManager, AuthPlugin

class TestPluginManagerGetAuthPlugin(unittest.TestCase):
    def setUp(self):
        self.manager = PluginManager()

    @patch('httpie.plugins.manager.PluginManager.get_auth_plugin_mapping')
    def test_valid_input(self, mock_get_auth_plugin_mapping):
        # Mock the return value of get_auth_plugin_mapping to simulate a valid mapping
        auth_plugin_mock = type('AuthPluginMock', (AuthPlugin,), {})
        mock_get_auth_plugin_mapping.return_value = {'exampleType': auth_plugin_mock}

        # Call the method under test
        result = self.manager.get_auth_plugin(auth_type="exampleType")

        # Assert that the correct AuthPlugin subclass is returned
        self.assertIsInstance(result, type(auth_plugin_mock))
