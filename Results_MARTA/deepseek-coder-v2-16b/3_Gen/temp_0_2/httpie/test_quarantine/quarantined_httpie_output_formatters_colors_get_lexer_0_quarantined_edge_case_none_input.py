
import pytest
from unittest.mock import patch, MagicMock
from pygments.lexers import TextLexer, JsonLexer
from httpie.output.formatters.colors import get_lexer

@pytest.mark.parametrize("mime, explicit_json, body, expected", [
    ("text/plain", False, "", None),
    ("application/json", True, '{"key": "value"}', JsonLexer),
    ("application/json", False, '{"key": "value"}', JsonLexer),
    ("text/html", False, "", TextLexer),
])
def test_get_lexer(mime, explicit_json, body, expected):
    with patch('pygments.lexers.get_lexer_for_mimetype') as mock_get_lexer_for_mimetype:
        with patch('pygments.lexers.get_lexer_by_name') as mock_get_lexer_by_name:
            if expected == JsonLexer:
                mock_get_lexer_by_name.return_value = JsonLexer(encoding='utf-8')
            elif expected is None:
                pass  # No lexer should be returned in this case
            else:
                mock_get_lexer_for_mimetype.return_value = expected

            result = get_lexer(mime, explicit_json, body)

            if expected == JsonLexer:
                assert isinstance(result, JsonLexer)
            elif expected is None:
                assert result is None
            else:
                assert isinstance(result, expected)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_formatters_colors_get_lexer_0_test_edge_case_none_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_get_lexer_0_test_edge_case_none_input.py:4:0: E0611: No name 'TextLexer' in module 'pygments.lexers' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_get_lexer_0_test_edge_case_none_input.py:4:0: E0611: No name 'JsonLexer' in module 'pygments.lexers' (no-name-in-module)


"""