
import re
from httpie.output.lexers.http import http_response_type
from unittest.mock import patch, MagicMock

def test_edge_case():
    lexer = MagicMock()
    match = re.match(r"HTTP/1\.1 (\d{3}) (.+)", "HTTP/1\.1 200 OK")
    ctx = {}
    
    with patch('httpie.output.lexers.http.pygments', autospec=True) as mock_pygments:
        mock_lexer = MagicMock()
        mock_pygments.lexer.bygroups.return_value = lambda *args, **kwargs: [("status_type", "text", "status_type")]
        
        result = list(http_response_type(lexer, match, ctx))
        
        assert len(result) == 1
        assert isinstance(result[0], tuple)
        assert result[0][0] == "status_type"
        assert result[0][1] == "text"
        assert result[0][2] == "status_type"

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
_ ERROR collecting Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_lexers_http_http_response_type_0_test_edge_case.py _
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_lexers_http_http_response_type_0_test_edge_case.py:3: in <module>
    from httpie.output.lexers.http import http_response_type
httpie/httpie/output/lexers/http.py:8: in <module>
    '1': pygments.token.Number.HTTP.INFO,
E   AttributeError: module 'pygments' has no attribute 'token'
=============================== warnings summary ===============================
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_lexers_http_http_response_type_0_test_edge_case.py:8
  /projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_lexers_http_http_response_type_0_test_edge_case.py:8: DeprecationWarning: invalid escape sequence '\.'
    match = re.match(r"HTTP/1\.1 (\d{3}) (.+)", "HTTP/1\.1 200 OK")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_lexers_http_http_response_type_0_test_edge_case.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 0.24s ==========================
"""