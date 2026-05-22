
import re
from httpie.output.lexers.http import http_response_type
import pytest
from unittest.mock import patch, MagicMock

@pytest.mark.parametrize("status_code, text, reason", [
    ("200", "OK", None),  # Example test case with a valid status code and phrase
])
def test_http_response_type(status_code, text, reason):
    # Create a mock lexer object
    lexer = MagicMock()
    
    # Create a match object for the regex to be used in the function
    match = re.match("HTTP/1\.1 (\d{3}) (.+)", f"HTTP/1\.1 {status_code} {text}")
    
    # Create an empty context object
    ctx = {}
    
    with patch('httpie.output.lexers.http.pygments', autospec=True):
        result = list(http_response_type(lexer, match, ctx))
        
        assert len(result) == 1
        group = result[0]
        assert isinstance(group, tuple)
        status_type, _, _ = group
        assert hasattr(status_type, 'name') and status_type.name == 'Number'

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
_ ERROR collecting Test4DT_tests_codestral/test_httpie_output_lexers_http_http_response_type_0_test_valid_input.py _
httpie/Test4DT_tests_codestral/test_httpie_output_lexers_http_http_response_type_0_test_valid_input.py:3: in <module>
    from httpie.output.lexers.http import http_response_type
httpie/httpie/output/lexers/http.py:8: in <module>
    '1': pygments.token.Number.HTTP.INFO,
E   AttributeError: module 'pygments' has no attribute 'token'
=============================== warnings summary ===============================
httpie/Test4DT_tests_codestral/test_httpie_output_lexers_http_http_response_type_0_test_valid_input.py:15
httpie/Test4DT_tests_codestral/test_httpie_output_lexers_http_http_response_type_0_test_valid_input.py:15
  /projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_codestral/test_httpie_output_lexers_http_http_response_type_0_test_valid_input.py:15: DeprecationWarning: invalid escape sequence '\.'
    match = re.match("HTTP/1\.1 (\d{3}) (.+)", f"HTTP/1\.1 {status_code} {text}")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_codestral/test_httpie_output_lexers_http_http_response_type_0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 2 warnings, 1 error in 0.22s =========================
"""