
import pytest
from httpie.status import http_status_to_exit_status, ExitStatus

def test_edge_cases():
    # Test None input
    with pytest.raises(TypeError):
        http_status_to_exit_status(None)
    
    # Test invalid integer input
    with pytest.raises(ValueError):
        http_status_to_exit_status("invalid")

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_status_http_status_to_exit_status_2_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None input
        with pytest.raises(TypeError):
            http_status_to_exit_status(None)
    
        # Test invalid integer input
        with pytest.raises(ValueError):
>           http_status_to_exit_status("invalid")

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_status_http_status_to_exit_status_2_test_edge_cases.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

http_status = 'invalid', follow = False

    def http_status_to_exit_status(http_status: int, follow=False) -> ExitStatus:
        """
        Translate HTTP status code to exit status code.
    
        (Relevant only when invoked with --check-status or --download.)
    
        """
>       if 300 <= http_status <= 399 and not follow:
E       TypeError: '<=' not supported between instances of 'int' and 'str'

httpie/httpie/status.py:30: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_status_http_status_to_exit_status_2_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.12s ===============================
"""