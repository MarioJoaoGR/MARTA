
import pytest
from unittest.mock import patch
from httpie.output.lexers.http import http_response_type

def test_http_response_type():
    with patch('httpie.output.lexers.http.pygments') as mock_pygments:
        # Mocking the necessary attributes and methods of pygments for testing
        mock_pygments.token = type('Token', (object,), {'Number': type('NumberType', (object,), {'HTTP': type('HTTPType', (object,), {'INFO': 'info_type'})})})()
        
        lexer = type('Lexer', (object,), {'precise': lambda self, token_type: token_type})()
        match = type('Match', (object,), {'group': lambda self: 'HTTP/1.1 200 OK'})()
        ctx = {}
        
        result = list(http_response_type(lexer, match, ctx))
        
        assert len(result) == 3  # Check if the generator yields three groups
        assert all(isinstance(group[0], mock_pygments.token.Number.HTTP.INFO.__class__) for group in result)  # Check if status_type is of expected type

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
_ ERROR collecting Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_lexers_http_http_response_type_0_test_edge_case.py _
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_lexers_http_http_response_type_0_test_edge_case.py:4: in <module>
    from httpie.output.lexers.http import http_response_type
httpie/httpie/output/lexers/http.py:8: in <module>
    '1': pygments.token.Number.HTTP.INFO,
E   AttributeError: module 'pygments' has no attribute 'token'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_lexers_http_http_response_type_0_test_edge_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.24s ===============================
"""