
import unittest
from httpie.plugins.manager import PluginManager
from typing import List, Type
from httpie.plugins.formatter_plugin import FormatterPlugin
from unittest.mock import patch

class TestPluginManagerGetFormatters(unittest.TestCase):
    
    @patch('httpie.plugins.manager.FormatterPlugin')
    def test_get_formatters(self, MockFormatterPlugin):
        # Arrange
        manager = PluginManager()
        
        # Act
        formatters = manager.get_formatters()
        
        # Assert
        self.assertIsInstance(formatters, List)
        self.assertIn(MockFormatterPlugin, formatters)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_manager_PluginManager_get_formatters_2_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_get_formatters_2_test_valid_inputs.py:5:0: E0401: Unable to import 'httpie.plugins.formatter_plugin' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_manager_PluginManager_get_formatters_2_test_valid_inputs.py:5:0: E0611: No name 'formatter_plugin' in module 'httpie.plugins' (no-name-in-module)


"""