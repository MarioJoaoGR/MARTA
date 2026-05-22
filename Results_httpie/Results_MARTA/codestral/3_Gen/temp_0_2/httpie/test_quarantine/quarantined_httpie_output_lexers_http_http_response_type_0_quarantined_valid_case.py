
import re
from httpie.output.lexers.http import http_response_type
import pytest
from unittest.mock import patch
from pygments.lexer import bygroups
from pygments.token import Number, Text

# Define a mock lexer for testing purposes
class MockLexer:
    def __init__(self):
        self.precise = False

    def get_tokens(self, text):
        return [(Number, '200'), (Text, ' '), (Number, '200')]

# Define a mock context for testing purposes
class MockContext:
    pass

@pytest.fixture
def setup_mocks():
    with patch('httpie.output.lexers.http.get_lexer_for_filename', return_value=MockLexer()):
        yield

def test_valid_case(setup_mocks):
    lexer = MockLexer()
    match = re.match(r"HTTP/1\.1 (\d{3}) (.+)", "HTTP/1\.1 200 OK")
    ctx = MockContext()
    
    result = list(http_response_type(lexer, match, ctx))
    
    assert len(result) == 3
    assert all(isinstance(token[0], Number) for token in result)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests_codestral/test_httpie_output_lexers_http_http_response_type_0_test_valid_case.py _
httpie/Test4DT_tests_codestral/test_httpie_output_lexers_http_http_response_type_0_test_valid_case.py:3: in <module>
    from httpie.output.lexers.http import http_response_type
httpie/httpie/output/lexers/http.py:8: in <module>
    '1': pygments.token.Number.HTTP.INFO,
E   AttributeError: module 'pygments' has no attribute 'token'
=============================== warnings summary ===============================
httpie/Test4DT_tests_codestral/test_httpie_output_lexers_http_http_response_type_0_test_valid_case.py:28
  /projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_codestral/test_httpie_output_lexers_http_http_response_type_0_test_valid_case.py:28: DeprecationWarning: invalid escape sequence '\.'
    match = re.match(r"HTTP/1\.1 (\d{3}) (.+)", "HTTP/1\.1 200 OK")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_codestral/test_httpie_output_lexers_http_http_response_type_0_test_valid_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 0.14s ==========================
"""