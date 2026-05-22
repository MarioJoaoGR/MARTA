
import unittest
from unittest.mock import patch
from httpie.output.lexers.common import Lexer  # Importing Lexer from the correct module

def precise(lexer, precise_token, parent_token):
    if precise_token is None or not lexer.options.get("precise"):
        return parent_token
    else:
        return precise_token

class TestPreciseFunction(unittest.TestCase):
    
    @patch('httpie.output.lexers.common.Lexer')  # Mocking the Lexer class from the correct module
    def test_precise_with_enabled_precise(self, mock_lexer):
        mock_lexer_instance = mock_lexer.return_value
        mock_lexer_instance.options = {"precise": True}
        
        result = precise(mock_lexer_instance, "CUSTOM_TOKEN", "DEFAULT_TOKEN")
        self.assertEqual(result, "CUSTOM_TOKEN")
    
    @patch('httpie.output.lexers.common.Lexer')  # Mocking the Lexer class from the correct module
    def test_precise_with_disabled_or_none_precise(self, mock_lexer):
        mock_lexer_instance = mock_lexer.return_value
        
        # Test with precise disabled or not set
        mock_lexer_instance.options = {}
        result = precise(mock_lexer_instance, "CUSTOM_TOKEN", "DEFAULT_TOKEN")
        self.assertEqual(result, "DEFAULT_TOKEN")
        
        # Test with precise_token as None
        mock_lexer_instance.options = {"precise": False}
        result = precise(mock_lexer_instance, None, "DEFAULT_TOKEN")
        self.assertEqual(result, "DEFAULT_TOKEN")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_lexers_common_precise_4_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_lexers_common_precise_4_test_valid_inputs.py:4:0: E0611: No name 'Lexer' in module 'httpie.output.lexers.common' (no-name-in-module)


"""