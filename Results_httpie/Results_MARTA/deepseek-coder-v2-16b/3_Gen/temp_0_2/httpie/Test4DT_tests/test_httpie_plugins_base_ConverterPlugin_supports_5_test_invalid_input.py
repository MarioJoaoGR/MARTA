
import unittest
from httpie.plugins.base import ConverterPlugin

class TestConverterPlugin(unittest.TestCase):
    def test_supports_invalid_input(self):
        with self.assertRaises(NotImplementedError):
            ConverterPlugin.supports("application/invalid-mime")
