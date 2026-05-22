
import unittest
from unittest.mock import patch, MagicMock
from httpie.output.processing import Formatting, Environment
from httpie.plugin_manager import get_formatters_grouped

class TestFormattingInit(unittest.TestCase):
    @patch('httpie.plugin_manager.get_formatters_grouped')
    def test_valid_input(self, mock_get_formatters_grouped):
        # Mock the return value of get_formatters_grouped
        mock_get_formatters_grouped.return_value = {
            'html': [MagicMock(), MagicMock()],
            'csv': [MagicMock()]
        }
        
        # Create an instance of Formatting with valid input
        formatting = Formatting(groups=['html', 'csv'], env=Environment())
        
        # Assert that the enabled_plugins list is populated correctly
        self.assertEqual(len(formatting.enabled_plugins), 3)
        for plugin in formatting.enabled_plugins:
            self.assertTrue(plugin.enabled)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_processing_Formatting___init___0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_output_processing_Formatting___init___0_test_valid_input.py:5:0: E0401: Unable to import 'httpie.plugin_manager' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_processing_Formatting___init___0_test_valid_input.py:5:0: E0611: No name 'plugin_manager' in module 'httpie' (no-name-in-module)


"""