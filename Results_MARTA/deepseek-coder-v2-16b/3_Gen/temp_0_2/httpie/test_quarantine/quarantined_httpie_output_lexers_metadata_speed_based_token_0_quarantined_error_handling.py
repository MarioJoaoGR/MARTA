
import pytest
from unittest.mock import patch
from httpie.output.lexers.metadata import speed_based_token
from pygments import lexers, token_types
import re

# Define a sample SPEED_TOKENS dictionary for testing purposes
SPEED_TOKENS = {
    10: lexers.PythonLexer(),
    20: lexers.HtmlLexer()
}

@pytest.mark.parametrize("lexer, match, ctx", [
    (lexers.PythonLexer(), re.match(r'\d+', "123 def main():"), {"line": 1})
])
def test_speed_based_token(lexer, match, ctx):
    with patch('httpie.output.lexers.metadata.SPEED_TOKENS', SPEED_TOKENS):
        results = list(speed_based_token(lexer, match, ctx))
        assert len(results) == 1
        start_pos, response_type, content = results[0]
        assert isinstance(response_type, type(pygments.token.Number))
        assert content == "123"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_lexers_metadata_speed_based_token_0_test_error_handling
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_lexers_metadata_speed_based_token_0_test_error_handling.py:5:0: E0611: No name 'token_types' in module 'pygments' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_lexers_metadata_speed_based_token_0_test_error_handling.py:10:8: E1101: Module 'pygments.lexers' has no 'PythonLexer' member (no-member)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_lexers_metadata_speed_based_token_0_test_error_handling.py:11:8: E1101: Module 'pygments.lexers' has no 'HtmlLexer' member (no-member)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_lexers_metadata_speed_based_token_0_test_error_handling.py:15:5: E1101: Module 'pygments.lexers' has no 'PythonLexer' member (no-member)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_lexers_metadata_speed_based_token_0_test_error_handling.py:22:46: E0602: Undefined variable 'pygments' (undefined-variable)


"""