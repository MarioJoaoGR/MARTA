
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.colors import get_lexer
from pygments.lexers import TextLexer, JsonLexer
from pygments import lexers
from typing import Optional, Type

def test_get_lexer_text_plain():
    with patch('httpie.output.formatters.colors.pygments.lexers.get_lexer_for_mimetype', return_value=TextLexer()):
        lexer = get_lexer('text/plain', explicit_json=False)
        assert isinstance(lexer, TextLexer)

def test_get_lexer_application_json():
    with patch('httpie.output.formatters.colors.pygments.lexers.get_lexer_for_mimetype', return_value=JsonLexer()):
        lexer = get_lexer('application/json', explicit_json=True, body='{"key": "value"}')
        assert isinstance(lexer, JsonLexer)

def test_get_lexer_explicit_json():
    with patch('httpie.output.formatters.colors.pygments.lexers.get_lexer_by_name', return_value=JsonLexer()):
        lexer = get_lexer('text/plain', explicit_json=True, body='{"key": "value"}')
        assert isinstance(lexer, JsonLexer)

def test_get_lexer_invalid_json():
    with patch('httpie.output.formatters.colors.pygments.lexers.get_lexer_by_name', return_value=TextLexer()):
        lexer = get_lexer('text/plain', explicit_json=True, body='invalid json')
        assert isinstance(lexer, TextLexer)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain.py:5:0: E0611: No name 'TextLexer' in module 'pygments.lexers' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_get_lexer_0_test_valid_case_text_plain.py:5:0: E0611: No name 'JsonLexer' in module 'pygments.lexers' (no-name-in-module)


"""