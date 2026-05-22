
import pytest
from unittest.mock import patch
from httpie.output.formatters.colors import ColorFormatter
from pygments.lexers import get_lexer_for_mimetype, JsonLexer

def test_get_lexer_for_body():
    # Create a mock environment with colors support for testing purposes
    class MockEnvironment:
        def __init__(self, colors=256):
            self.colors = colors
    
    env = MockEnvironment(colors=256)
    
    # Initialize the ColorFormatter with the mock environment
    formatter = ColorFormatter(env=env, explicit_json=True, color_scheme='default')
    
    # Define a MIME type and body content for testing
    mime_type = 'application/json'
    json_body = '{"key": "value"}'
    
    with patch('httpie.output.formatters.colors.get_lexer_for_mimetype') as mock_get_lexer:
        # Configure the mock to return JsonLexer when called with 'application/json'
        mock_get_lexer.return_value = JsonLexer
        
        # Call the method under test
        lexer = formatter.get_lexer_for_body(mime_type, json_body)
        
        # Assert that the correct lexer was returned
        assert isinstance(lexer, JsonLexer)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_colors_ColorFormatter_get_lexer_for_body_0_test_valid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_ColorFormatter_get_lexer_for_body_0_test_valid_input.py:5:0: E0611: No name 'JsonLexer' in module 'pygments.lexers' (no-name-in-module)


"""