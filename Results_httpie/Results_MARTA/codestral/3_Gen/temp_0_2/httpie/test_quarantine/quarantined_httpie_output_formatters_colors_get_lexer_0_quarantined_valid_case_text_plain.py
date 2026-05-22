
import unittest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.colors import get_lexer
from pygments.lexers import ClassNotFound
from pygments.lexers import TextLexer, JsonLexer
import json

class TestGetLexer(unittest.TestCase):
    
    @patch('pygments.lexers.get_lexer_for_mimetype')
    @patch('pygments.lexers.get_lexer_by_name')
    def test_valid_case_text_plain(self, mock_get_lexer_by_name, mock_get_lexer_for_mimetype):
        # Mock the lexer return values
        mock_get_lexer_for_mimetype.side_effect = ClassNotFound()
        mock_get_lexer_by_name.side_effect = [TextLexer]
        
        # Test for text/plain mime type
        result = get_lexer('text/plain', explicit_json=False)
        self.assertIsInstance(result, TextLexer)
        
        # Mock the lexer return values again
        mock_get_lexer_for_mimetype.side_effect = ClassNotFound()
        mock_get_lexer_by_name.side_effect = [TextLexer]
        
        # Test for application/json mime type with explicit JSON flag
        result = get_lexer('application/json', explicit_json=True, body='{"key": "value"}')
        self.assertIsInstance(result, JsonLexer)
        
        # Mock the lexer return values again
        mock_get_lexer_for_mimetype.side_effect = ClassNotFound()
        mock_get_lexer_by_name.side_effect = [TextLexer]
        
        # Test for application/json mime type without explicit JSON flag but with valid JSON body
        result = get_lexer('application/json', explicit_json=False, body='{"key": "value"}')
        self.assertIsInstance(result, JsonLexer)
        
        # Mock the lexer return values again
        mock_get_lexer_for_mimetype.side_effect = ClassNotFound()
        mock_get_lexer_by_name.side_effect = [TextLexer]
        
        # Test for application/json mime type with invalid JSON body
        result = get_lexer('application/json', explicit_json=True, body='invalid json')
        self.assertIsInstance(result, JsonLexer)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain.py:6:0: E0611: No name 'TextLexer' in module 'pygments.lexers' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain.py:6:0: E0611: No name 'JsonLexer' in module 'pygments.lexers' (no-name-in-module)


"""