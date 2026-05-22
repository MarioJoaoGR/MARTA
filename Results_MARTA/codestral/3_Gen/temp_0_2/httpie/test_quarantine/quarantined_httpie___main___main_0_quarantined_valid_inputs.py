
import pytest
from unittest.mock import patch
from httpie.__main__ import main as httpie_main

def test_valid_inputs():
    with patch('httpie.core.main', return_value=0):
        assert httpie_main() == 0

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

httpie/Test4DT_tests_codestral/test_httpie___main___main_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        with patch('httpie.core.main', return_value=0):
>           assert httpie_main() == 0

httpie/Test4DT_tests_codestral/test_httpie___main___main_0_test_valid_inputs.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def main():
        try:
            from httpie.core import main
            exit_status = main()
        except KeyboardInterrupt:
            from httpie.status import ExitStatus
            exit_status = ExitStatus.ERROR_CTRL_C
    
>       return exit_status.value
E       AttributeError: 'int' object has no attribute 'value'

httpie/httpie/__main__.py:14: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie___main___main_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.28s ===============================
"""