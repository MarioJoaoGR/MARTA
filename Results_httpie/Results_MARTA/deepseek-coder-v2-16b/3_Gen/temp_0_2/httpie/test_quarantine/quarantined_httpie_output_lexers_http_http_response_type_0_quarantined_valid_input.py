
import pytest
from unittest.mock import patch
from httpie.output.lexers.http import http_response_type

def test_http_response_type():
    with patch('httpie.output.lexers.http.pygments') as mock_pygments:
        lexer = mock_pygments.lexers.get_lexer_for_filename("example.http")
        match = mock_pygments.re.match(r"HTTP/1\.1 (\d{3}) (.+)", "HTTP/1\.1 200 OK")
        ctx = {}
        
        result = list(http_response_type(lexer, match, ctx))
        
        assert len(result) == 3  # Check if the generator yields three groups
        assert isinstance(result[0], pygments.token.Token)  # Check if the first group is a Pygments token
        assert result[1] == "200 OK"  # Check if the text part matches the expected string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_lexers_http_http_response_type_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_lexers_http_http_response_type_0_test_valid_input.py:15:37: E0602: Undefined variable 'pygments' (undefined-variable)


"""