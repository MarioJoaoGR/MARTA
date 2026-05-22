
import unittest
from unittest.mock import patch, MagicMock
from httpie.output.processing import Conversion

class TestConversion(unittest.TestCase):
    
    @patch('httpie.output.processing.plugin_manager')
    def test_get_converter_invalid_mime(self, mock_plugin_manager):
        # Mock the plugin manager to return an empty list of converters
        mock_plugin_manager.get_converters.return_value = []
        
        conversion = Conversion()
        result = conversion.get_converter("invalid/mime")
        
        self.assertIsNone(result)
