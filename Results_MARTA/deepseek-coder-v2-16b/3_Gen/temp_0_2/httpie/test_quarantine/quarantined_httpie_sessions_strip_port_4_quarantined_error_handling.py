
import pytest
from unittest.mock import patch
from httpie.sessions import strip_port

def test_error_handling():
    with patch('builtins.print') as mock_print:
        # Test case for a valid string input
        assert strip_port("example.com") == "example.com"
    
        # Test case for an invalid input (non-string value)
        with pytest.raises(TypeError):
            strip_port(12345)  # This should raise a TypeError because the input is not a string

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_strip_port_4_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        with patch('builtins.print') as mock_print:
            # Test case for a valid string input
            assert strip_port("example.com") == "example.com"
    
            # Test case for an invalid input (non-string value)
            with pytest.raises(TypeError):
>               strip_port(12345)  # This should raise a TypeError because the input is not a string

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_strip_port_4_test_error_handling.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

hostname = 12345

    def strip_port(hostname: str) -> str:
>       return hostname.split(':')[0]
E       AttributeError: 'int' object has no attribute 'split'

httpie/httpie/sessions.py:57: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_sessions_strip_port_4_test_error_handling.py::test_error_handling
============================== 1 failed in 0.28s ===============================
"""