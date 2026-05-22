
import re
from httpie.output.lexers.http import http_response_type
import pytest
from unittest.mock import patch, MagicMock

@pytest.mark.parametrize("status_line, expected", [
    ("HTTP/1.1 200 OK", "INFO"),
    ("HTTP/1.1 404 Not Found", "ERROR"),
    ("HTTP/1.1 500 Internal Server Error", "ERROR"),
])
def test_http_response_type(status_line, expected):
    lexer = MagicMock()
    match = re.match(r"HTTP/1\.1 (\d{3}) (.+)", status_line)
    ctx = {}
    
    with patch('pygments.token', autospec=True) as mock_token:
        # Mock the precise function to return a specific token type based on the status code
        def precise(lexer, default_type, base_type):
            if int(match.group(1)) < 300:
                return getattr(mock_token, expected)
            else:
                return mock_token.Number
        
        with patch('httpie.output.lexers.http.precise', side_effect=precise):
            result = list(http_response_type(lexer, match, ctx))
            assert len(result) == 1
            assert isinstance(result[0][0], getattr(mock_token, expected))

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
_ ERROR collecting Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_lexers_http_http_response_type_0_test_error_handling.py _
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_lexers_http_http_response_type_0_test_error_handling.py:3: in <module>
    from httpie.output.lexers.http import http_response_type
httpie/httpie/output/lexers/http.py:8: in <module>
    '1': pygments.token.Number.HTTP.INFO,
E   AttributeError: module 'pygments' has no attribute 'token'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_lexers_http_http_response_type_0_test_error_handling.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.16s ===============================
"""