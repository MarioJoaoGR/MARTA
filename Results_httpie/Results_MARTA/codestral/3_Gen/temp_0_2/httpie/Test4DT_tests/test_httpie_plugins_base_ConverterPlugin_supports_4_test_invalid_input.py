
import unittest
from unittest.mock import patch
from httpie.plugins.base import ConverterPlugin

class TestConverterPlugin(unittest.TestCase):
    def test_supports_invalid_input(self):
        with patch.object(ConverterPlugin, 'supports', return_value=False) as mock_supports:
            plugin = ConverterPlugin("application/test-mime")
            self.assertFalse(plugin.supports("invalid-mime"))
