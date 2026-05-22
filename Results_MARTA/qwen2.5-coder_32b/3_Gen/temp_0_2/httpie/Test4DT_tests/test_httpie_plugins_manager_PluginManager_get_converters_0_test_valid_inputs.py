
import unittest
from httpie.plugins.manager import PluginManager
from unittest.mock import patch, MagicMock

class TestPluginManagerGetConverters(unittest.TestCase):
    
    @patch('httpie.plugins.manager.PluginManager.filter')
    def test_get_converters_valid_inputs(self, mock_filter):
        # Create a mock converter plugin class
        class MockConverterPlugin:
            pass
        
        # Set up the return value of filter method to be a list containing the MockConverterPlugin
        mock_filter.return_value = [MockConverterPlugin]
        
        # Instantiate PluginManager and call get_converters method
        manager = PluginManager()
        converters = manager.get_converters()
        
        # Assert that the returned value is a list containing MockConverterPlugin
        self.assertIsInstance(converters, list)
        self.assertIn(MockConverterPlugin, converters)
