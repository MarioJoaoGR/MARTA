
import re
from httpie.output.lexers.http import http_response_type

# Assuming RE_STATUS_LINE is a predefined regular expression for matching HTTP status lines
RE_STATUS_LINE = re.compile(r"HTTP/1\.1 (\d{3}) (.+)")

def precise(lexer, token_type, fallback_token):
    # This function should be defined based on the actual implementation of Pygments' `precise` functionality
    return token_type  # Placeholder for the actual logic

STATUS_TYPES = {
    '1': pygments.token.Number.HTTP.INFO,
    '2': pygments.token.Number.HTTP.SUCCESS,
    '3': pygments.token.Number.HTTP.REDIRECT,
    '4': pygments.token.Number.HTTP.CLIENT_ERROR,
    '5': pygments.token.Number.HTTP.SERVER_ERROR,
}

def http_response_type(lexer, match, ctx):
    status_match = RE_STATUS_LINE.match(match.group())
    if status_match is None:
        return None

    status_code, text, reason = status_match.groups()
    status_type = precise(
        lexer,
        STATUS_TYPES.get(status_code[0], pygments.token.Number),
        pygments.token.Number
    )

    groups = pygments.lexer.bygroups(
        status_type,
        pygments.token.Text,
        status_type
    )
    yield from groups(lexer, status_match, ctx)
```

### Test Case Code
```python
import pytest
from unittest.mock import patch
import httpie.output.lexers.http as lexer_module

@pytest.fixture(autouse=True)
def mock_pygments():
    with patch('httpie.output.lexers.http.pygments') as mock_pygments:
        yield mock_pygments

def test_http_response_type_invalid_input(mock_pygments):
    lexer = None  # Assuming a valid lexer object for the purpose of this example
    match = re.match(r"HTTP/1\.1 (\d{3}) (.+)", "HTTP/1\.1 200 OK")
    ctx = {}  # An empty context object, adjust as needed based on the lexer's requirements

    with pytest.warns(DeprecationWarning):
        result = list(lexer_module.http_response_type(lexer, match, ctx))
    
    assert result == []  # Adjust this assertion based on expected output or behavior

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_lexers_http_http_response_type_0_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_output_lexers_http_http_response_type_0_test_invalid_input.py:38:1: E0001: Parsing failed: 'invalid syntax (Test4DT_tests_codestral.test_httpie_output_lexers_http_http_response_type_0_test_invalid_input, line 38)' (syntax-error)


"""