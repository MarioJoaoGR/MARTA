
import pytest
from unittest.mock import MagicMock, patch
from httpie.output.formatters.colors import ColorFormatter
from httpie.environment import Environment
from pygments.lexers import get_lexer_for_mimetype
from pygments.formatter import Formatter
from pygments.token import Token

@pytest.fixture
def color_formatter():
    env = MagicMock()
    env.colors = 256  # Assuming the environment supports colors for this test
    return ColorFormatter(env=env, explicit_json=False, color_scheme='solarized-dark')

def test_format_body_with_lexer(color_formatter):
    with patch('pygments.highlight') as mock_highlight:
        # Mock the get_lexer_for_mimetype to return a lexer for a known MIME type
        with patch('pygments.lexers.get_lexer_for_mimetype', return_value=MagicMock()):
            body = "print('Hello, World!')"
            mime = "text/plain"
            result = color_formatter.format_body(body, mime)
            
            # Assert that the highlight function was called with the correct arguments
            mock_highlight.assert_called_once_with(
                code=body,
                lexer=get_lexer_for_mimetype(mime),
                formatter=color_formatter.body_formatter
            )
            
            # Assert that the result is not None (the mocked highlight function should return a string)
            assert result is not None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_formatters_colors_ColorFormatter_format_body_0_test_edge_case_none
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_ColorFormatter_format_body_0_test_edge_case_none.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_ColorFormatter_format_body_0_test_edge_case_none.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)


"""