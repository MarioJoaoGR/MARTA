
import unittest
from httpie.plugins.manager import PluginManager
from typing import List, Type
from unittest.mock import patch

class TestPluginManagerGetAuthPlugins(unittest.TestCase):
    
    @patch('httpie.plugins.manager.PluginManager.filter')
    def test_none_input(self, mock_filter):
        manager = PluginManager()
        
        # Mock the return value of filter method to be an empty list
        mock_filter.return_value = []
        
        auth_plugins = manager.get_auth_plugins()
        
        self.assertEqual(auth_plugins, [])
