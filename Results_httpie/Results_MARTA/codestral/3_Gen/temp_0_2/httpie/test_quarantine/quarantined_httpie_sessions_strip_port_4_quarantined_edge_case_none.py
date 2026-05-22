
from httpie.sessions import strip_port
from unittest.mock import patch

def test_edge_case_none():
    with patch('builtins.print') as mock_print:
        # Test None input
        result = strip_port(None)
        assert result is None, f"Expected None but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_sessions_strip_port_4_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        with patch('builtins.print') as mock_print:
            # Test None input
>           result = strip_port(None)

httpie/Test4DT_tests_codestral/test_httpie_sessions_strip_port_4_test_edge_case_none.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hostname = None

    def strip_port(hostname: str) -> str:
>       return hostname.split(':')[0]
E       AttributeError: 'NoneType' object has no attribute 'split'

httpie/httpie/sessions.py:57: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_sessions_strip_port_4_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.24s ===============================
"""