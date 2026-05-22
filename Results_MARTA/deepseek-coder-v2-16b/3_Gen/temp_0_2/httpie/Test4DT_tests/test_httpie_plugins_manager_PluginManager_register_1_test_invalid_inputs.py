
import unittest
from unittest.mock import patch
from httpie.plugins.manager import PluginManager

class TestPluginManagerRegister(unittest.TestCase):
    
    @patch('httpie.plugins.manager.PluginManager')
    def test_register_invalid_inputs(self, MockPluginManager):
        plugin_manager = MockPluginManager()
        
        # Registering invalid inputs should not raise an error
        try:
            plugin_manager.register(None)  # Passing None as a plugin (should be invalid)
        except TypeError:
            self.fail("Registering invalid input raised TypeError unexpectedly!")
