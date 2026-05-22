
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.colors import get_lexer
from pygments.lexers import JsonLexer, TextLexer
from pygments.util import ClassNotFound
import json

def test_get_lexer_invalid_mime():
    with pytest.raises(ClassNotFound):
        get_lexer('invalid/mime')

def test_get_lexer_json_explicitly():
    lexer = get_lexer('application/json', explicit_json=True, body='{"key": "value"}')
    assert isinstance(lexer, JsonLexer)

def test_get_lexer_text_implicitly():
    lexer = get_lexer('text/plain', explicit_json=False)
    assert isinstance(lexer, TextLexer)

@patch('pygments.lexers.get_lexer_for_mimetype')
@patch('pygments.lexers.get_lexer_by_name')
def test_get_lexer_fallback(mock_get_lexer_by_name, mock_get_lexer_for_mimetype):
    mock_get_lexer_for_mimetype.side_effect = ClassNotFound('test', 'error')
    lexer = get_lexer('application/json', explicit_json=False)
    assert isinstance(lexer, JsonLexer)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_colors_get_lexer_0_test_invalid_input_malformed_mime
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_invalid_input_malformed_mime.py:5:0: E0611: No name 'JsonLexer' in module 'pygments.lexers' (no-name-in-module)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_invalid_input_malformed_mime.py:5:0: E0611: No name 'TextLexer' in module 'pygments.lexers' (no-name-in-module)


"""