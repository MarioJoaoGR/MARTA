
import pytest
from httpie.manager.__main__ import program
from unittest.mock import patch

def test_invalid_inputs():
    with patch('httpie.manager.__main__.sys.argv', ['program', '--invalid-arg']):
        with pytest.raises(SystemExit) as excinfo:
            program()

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

httpie/Test4DT_tests_codestral/test_httpie_manager___main___program_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with patch('httpie.manager.__main__.sys.argv', ['program', '--invalid-arg']):
>           with pytest.raises(SystemExit) as excinfo:
E           Failed: DID NOT RAISE <class 'SystemExit'>

httpie/Test4DT_tests_codestral/test_httpie_manager___main___program_1_test_invalid_inputs.py:8: Failed
----------------------------- Captured stderr call -----------------------------
usage: httpie [-h] [--debug] [--traceback] [--version] {cli,plugins} ...
httpie: error: argument action: invalid choice: 'httpie/Test4DT_tests_codestral/test_httpie_manager___main___program_1_test_invalid_inputs.py' (choose from 'cli', 'plugins')
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_manager___main___program_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.31s ===============================
"""