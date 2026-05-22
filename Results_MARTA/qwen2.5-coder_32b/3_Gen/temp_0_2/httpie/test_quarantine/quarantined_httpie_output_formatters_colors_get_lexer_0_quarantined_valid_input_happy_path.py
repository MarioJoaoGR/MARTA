
import pytest
from unittest.mock import patch, MagicMock
from pygments.lexers import get_lexer_for_mimetype, get_lexer_by_name
from pygments.lexers.special import TextLexer
from pygments.lexers.json import JsonLexer
from httpie.output.formatters.colors import get_lexer

def test_get_lexer_with_valid_mime():
    with patch('pygments.lexers.get_lexer_for_mimetype') as mock_get_lexer:
        mock_get_lexer.return_value = MagicMock()
        lexer = get_lexer('text/plain', explicit_json=False)
        assert isinstance(lexer, type(mock_get_lexer.return_value))

def test_get_lexer_with_explicit_json():
    with patch('pygments.lexers.get_lexer_by_name') as mock_get_lexer:
        mock_get_lexer.side_effect = [None, JsonLexer()]
        lexer = get_lexer('application/json', explicit_json=True, body='{"key": "value"}')
        assert isinstance(lexer, JsonLexer)

def test_get_lexer_with_invalid_json():
    with patch('pygments.lexers.get_lexer_by_name') as mock_get_lexer:
        mock_get_lexer.side_effect = [None, TextLexer()]
        lexer = get_lexer('application/json', explicit_json=True, body='invalid json')
        assert isinstance(lexer, TextLexer)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_colors_get_lexer_0_test_valid_input_happy_path
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_valid_input_happy_path.py:6:0: E0401: Unable to import 'pygments.lexers.json' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_valid_input_happy_path.py:6:0: E0611: No name 'json' in module 'pygments.lexers' (no-name-in-module)


"""