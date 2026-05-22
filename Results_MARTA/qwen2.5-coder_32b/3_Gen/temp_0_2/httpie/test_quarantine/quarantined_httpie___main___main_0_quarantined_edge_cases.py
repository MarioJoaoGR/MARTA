
import pytest
from unittest.mock import patch
from httpie.__main__ import main as httpie_main
from httpie.status import ExitStatus

def test_main():
    with patch('httpie.__main__.main', return_value=0):
        result = httpie_main()
        assert result == ExitStatus.SUCCESS.value

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie___main___main_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
__________________________________ test_main ___________________________________

    def test_main():
        with patch('httpie.__main__.main', return_value=0):
            result = httpie_main()
>           assert result == ExitStatus.SUCCESS.value
E           assert 1 == 0
E            +  where 0 = <ExitStatus.SUCCESS: 0>.value
E            +    where <ExitStatus.SUCCESS: 0> = ExitStatus.SUCCESS

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie___main___main_0_test_edge_cases.py:10: AssertionError
----------------------------- Captured stderr call -----------------------------
usage:
    http [METHOD] URL [REQUEST_ITEM ...]

error:
    unrecognized arguments: --json-report 
--json-report-file=pytest_report_qwen2.5-coder_32b.json

for more information:
    run 'http --help' or visit https://httpie.io/docs/cli

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie___main___main_0_test_edge_cases.py::test_main
============================== 1 failed in 0.40s ===============================
"""