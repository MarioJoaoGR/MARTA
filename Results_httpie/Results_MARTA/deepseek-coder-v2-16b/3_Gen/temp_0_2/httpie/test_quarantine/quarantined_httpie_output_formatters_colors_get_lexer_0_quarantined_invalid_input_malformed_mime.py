
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.colors import get_lexer
from pygments.lexers import ClassNotFound
from pygments.lexers.special import TextLexer
from pygments.lexers.json import JsonLexer

def test_get_lexer_invalid_mime():
    with patch('httpie.output.formatters.colors.pygments.lexers.get_lexer_for_mimetype', side_effect=ClassNotFound):
        with patch('httpie.output.formatters.colors.pygments.lexers.get_lexer_by_name', side_effect=ClassNotFound):
            lexer = get_lexer('invalid/mime')
            assert isinstance(lexer, TextLexer)

def test_get_lexer_explicit_json():
    body = '{"key": "value"}'
    with patch('httpie.output.formatters.colors.pygments.lexers.get_lexer_by_name', side_effect=ClassNotFound):
        lexer = get_lexer('application/json', explicit_json=True, body=body)
        assert isinstance(lexer, JsonLexer)

def test_get_lexer_enhanced_json():
    body = '{"key": "value"}'
    with patch('httpie.output.formatters.colors.pygments.lexers.get_lexer_by_name', side_effect=ClassNotFound):
        lexer = get_lexer('application/json', explicit_json=True, body=body)
        assert isinstance(lexer, EnhancedJsonLexer)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_formatters_colors_get_lexer_0_test_invalid_input_malformed_mime
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_get_lexer_0_test_invalid_input_malformed_mime.py:7:0: E0401: Unable to import 'pygments.lexers.json' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_get_lexer_0_test_invalid_input_malformed_mime.py:7:0: E0611: No name 'json' in module 'pygments.lexers' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_get_lexer_0_test_invalid_input_malformed_mime.py:25:33: E0602: Undefined variable 'EnhancedJsonLexer' (undefined-variable)


"""