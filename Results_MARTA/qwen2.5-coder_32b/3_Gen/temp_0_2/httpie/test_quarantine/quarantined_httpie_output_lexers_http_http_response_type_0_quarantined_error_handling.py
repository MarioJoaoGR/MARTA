
import re
from httpie.output.lexers.http import http_response_type
import pytest
from unittest.mock import patch, MagicMock

@pytest.mark.parametrize("lexer, match, ctx", [
    (MagicMock(), re.match(r"HTTP/1\.1 (\d{3}) (.+)", "HTTP/1\.1 200 OK"), {}),
])
def test_http_response_type(lexer, match, ctx):
    with patch('httpie.output.lexers.http.precise', return_value=pygments.token.Number):
        result = list(http_response_type(lexer, match, ctx))
        assert len(result) == 3  # Check if the length of the yielded groups is correct

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_lexers_http_http_response_type_0_test_error_handling
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_lexers_http_http_response_type_0_test_error_handling.py:11:65: E0602: Undefined variable 'pygments' (undefined-variable)


"""