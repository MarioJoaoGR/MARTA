
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.colors import ColorFormatter
from httpie.environment import Environment

@pytest.fixture(autouse=True)
def setup_color_formatter():
    # Setup the environment to support colors for testing purposes
    env = Environment()
    env.colors = 256  # Assuming this is what we want to test with
    yield ColorFormatter(env=env, color_scheme='solarized-dark')

def test_format_body_with_valid_mime():
    formatter = pytest.fixture_setup_color_formatter()
    body = "print('Hello, World!')"
    mime = 'text/plain'  # Example MIME type for a plain text

    with patch('httpie.output.formatters.colors.pygments.highlight') as mock_highlight:
        expected_highlighted_body = "highlighted body"
        mock_highlight.return_value = expected_highlighted_body

        result = formatter.format_body(body, mime)

        assert result == expected_highlighted_body
        mock_highlight.assert_called_once_with(
            code=body,
            lexer=formatter.get_lexer_for_body(mime, body),
            formatter=formatter.body_formatter,
        )

def test_format_body_without_valid_mime():
    formatter = pytest.fixture_setup_color_formatter()
    body = "print('Hello, World!')"
    mime = 'invalid/mime'  # An invalid MIME type to trigger no lexer scenario

    result = formatter.format_body(body, mime)

    assert result == body  # The original body should be returned unchanged if no lexer is found

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_formatters_colors_ColorFormatter_format_body_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_ColorFormatter_format_body_0_test_valid_input.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_ColorFormatter_format_body_0_test_valid_input.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_ColorFormatter_format_body_0_test_valid_input.py:15:16: E1101: Module 'pytest' has no 'fixture_setup_color_formatter' member (no-member)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_ColorFormatter_format_body_0_test_valid_input.py:33:16: E1101: Module 'pytest' has no 'fixture_setup_color_formatter' member (no-member)


"""