
import pytest
from unittest.mock import patch, MagicMock
from pygments.lexers import get_lexer_for_mimetype, get_lexer_by_name
from pygments.lexers.special import TextLexer
from pygments.lexers.json import JsonLexer
from httpie.output.formatters.colors import get_lexer

def test_get_lexer_default():
    with patch('pygments.lexers.get_lexer_for_mimetype', return_value=MagicMock()):
        lexer = get_lexer('text/plain', explicit_json=False)
        assert isinstance(lexer, MagicMock)

def test_get_lexer_explicit_json():
    body = '{"key": "value"}'
    with patch('pygments.lexers.get_lexer_by_name', return_value=JsonLexer()):
        lexer = get_lexer('application/json', explicit_json=True, body=body)
        assert isinstance(lexer, JsonLexer)

def test_get_lexer_explicit_json_invalid():
    body = 'not a valid json'
    with patch('pygments.lexers.get_lexer_by_name', side_effect=[TextLexer(), JsonLexer()]):
        lexer = get_lexer('application/json', explicit_json=True, body=body)
        assert isinstance(lexer, JsonLexer)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_colors_get_lexer_0_test_edge_case_none_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_edge_case_none_input.py:6:0: E0401: Unable to import 'pygments.lexers.json' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_edge_case_none_input.py:6:0: E0611: No name 'json' in module 'pygments.lexers' (no-name-in-module)


"""