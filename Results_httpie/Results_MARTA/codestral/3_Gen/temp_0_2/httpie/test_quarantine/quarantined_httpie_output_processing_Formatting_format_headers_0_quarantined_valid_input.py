
import unittest
from httpie.output.processing import Formatting
from httpie.plugins import plugin_manager
from unittest.mock import patch, MagicMock

class TestFormatting(unittest.TestCase):
    @patch('httpie.plugins.plugin_manager.get_formatters_grouped')
    def test_valid_input(self, mock_get_formatters_grouped):
        # Mock the available plugins and their enabled state
        mock_env = MagicMock()
        mock_formatter1 = MagicMock()
        mock_formatter2 = MagicMock()
        
        # Configure mocks to return expected results
        mock_get_formatters_grouped.return_value = {
            'test_group': [mock_formatter1, mock_formatter2]
        }
        
        # Set the enabled state for the formatters
        mock_formatter1.enabled = True
        mock_formatter2.enabled = False
        
        # Create an instance of Formatting with a valid group and environment
        formatting = Formatting(groups=['test_group'], env=mock_env)
        
        # Define the expected formatted headers
        expected_headers = "formatted_headers"
        
        # Mock the format_headers method for both enabled formatters
        mock_formatter1.format_headers.return_value = expected_headers
        mock_formatter2.format_headers.return_value = expected_headers  # Even if not used, it should be consistent with the first formatter's output
        
        # Call the method under test
        result = formatting.format_headers("raw_headers")
        
        # Assert that the format_headers method was called on all enabled plugins
        mock_formatter1.format_headers.assert_called_once_with("raw_headers")
        mock_formatter2.format_headers.assert_not_called()  # Ensure the disabled formatter is not called
        
        # Assert that the result matches the expected formatted headers
        self.assertEqual(result, expected_headers)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_processing_Formatting_format_headers_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_output_processing_Formatting_format_headers_0_test_valid_input.py:4:0: E0611: No name 'plugin_manager' in module 'httpie.plugins' (no-name-in-module)


"""