
import unittest
from httpie.plugins.base import ConverterPlugin

class TestConverterPluginSupports(unittest.TestCase):
    def test_none_input(self):
        with self.assertRaises(NotImplementedError):
            ConverterPlugin.supports("application/test-mime")
