
import unittest
from httpie.plugins.manager import PluginManager
from unittest.mock import patch

class TestPluginManager(unittest.TestCase):
    
    @patch('httpie.plugins.manager.PluginManager.append')
    def test_register_valid_inputs(self, mock_append):
        plugin_manager = PluginManager()
        ExamplePlugin = type('ExamplePlugin', (object,), {'__module__': 'example_plugin'})
        
        plugin_manager.register(ExamplePlugin)
        
        mock_append.assert_called_once_with(ExamplePlugin)
