
import pytest
from unittest.mock import patch, MagicMock
from pygments.lexers import get_lexer_for_mimetype, get_lexer_by_name
from pygments.lexers.special import TextLexer
from pygments.lexers.json import JsonLexer
from httpie.output.formatters.colors import get_lexer
import json

def test_get_lexer():
    # Test with a text/plain MIME type
    lexer = get_lexer('text/plain', explicit_json=False)
    assert isinstance(lexer, TextLexer)

    # Test with an application/json MIME type and explicit JSON content
    lexer = get_lexer('application/json', explicit_json=True, body='{"key": "value"}')
    assert isinstance(lexer, JsonLexer)

    # Test with a non-JSON MIME type but explicitly set as JSON
    lexer = get_lexer('text/html', explicit_json=True, body='<html></html>')
    assert isinstance(lexer, JsonLexer)  # Should fallback to JSON lexer due to explicit flag

    # Test with a valid JSON content and correct MIME type
    lexer = get_lexer('application/json', explicit_json=False, body='{"key": "value"}')
    assert isinstance(lexer, JsonLexer)

    # Test with an invalid JSON content but correct MIME type
    with pytest.raises(ValueError):
        get_lexer('application/json', explicit_json=True, body='invalid json')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_colors_get_lexer_0_test_edge_case_none
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_edge_case_none.py:6:0: E0401: Unable to import 'pygments.lexers.json' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_lexer_0_test_edge_case_none.py:6:0: E0611: No name 'json' in module 'pygments.lexers' (no-name-in-module)


"""