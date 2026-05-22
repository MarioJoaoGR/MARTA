
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.colors import ColorFormatter
from pygments import highlight
from pygments.lexers import get_lexer_for_mimetype
from pygments.formatters import TerminalFormatter

@pytest.fixture
def color_formatter():
    env = MagicMock()
    env.colors = 256  # Assuming the environment supports 256 colors for this test
    return ColorFormatter(env=env, explicit_json=True, color_scheme='default')

def test_format_body_with_lexer(color_formatter):
    with patch('httpie.output.formatters.colors.get_lexer_for_mimetype', return_value=None) as mock_lexer:
        # Test with an invalid mime type that does not have a corresponding lexer
        body = "print('Hello, world!')"
        formatted_body = color_formatter.format_body(body, 'invalid/mime')
        
        # Assert that the original body is returned if no lexer is found
        assert formatted_body == body
        mock_lexer.assert_called_with('invalid/mime', body)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_colors_ColorFormatter_format_body_1_test_invalid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_ColorFormatter_format_body_1_test_invalid_input.py:7:0: E0611: No name 'TerminalFormatter' in module 'pygments.formatters' (no-name-in-module)


"""