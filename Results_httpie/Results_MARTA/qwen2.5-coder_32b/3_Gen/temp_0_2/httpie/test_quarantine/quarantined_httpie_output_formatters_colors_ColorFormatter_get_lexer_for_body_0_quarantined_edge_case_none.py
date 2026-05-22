
import pytest
from unittest.mock import patch
from httpie.output.formatters.colors import ColorFormatter
from pygments.lexers import get_lexer_for_mimetype, TextLexer

@pytest.fixture
def setup_color_formatter():
    env = type('Environment', (object,), {'colors': True})()
    return ColorFormatter(env=env)

def test_get_lexer_for_body_none(setup_color_formatter):
    with patch('httpie.output.formatters.colors.get_lexer_for_mimetype', return_value=None):
        lexer = setup_color_formatter.get_lexer_for_body('application/unknown', 'some body content')
        assert lexer is None, "Expected get_lexer_for_body to return None when no lexer is found."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_colors_ColorFormatter_get_lexer_for_body_0_test_edge_case_none
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_ColorFormatter_get_lexer_for_body_0_test_edge_case_none.py:5:0: E0611: No name 'TextLexer' in module 'pygments.lexers' (no-name-in-module)


"""