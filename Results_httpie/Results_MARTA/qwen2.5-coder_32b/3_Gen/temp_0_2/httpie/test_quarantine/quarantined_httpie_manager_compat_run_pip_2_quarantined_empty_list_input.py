
import pytest
from unittest.mock import patch
from httpie.manager.compat import run_pip

def test_run_pip_empty_list():
    with patch('httpie.manager.compat.run_pip', return_value=b'output'):
        result = run_pip([])
        assert result == b'output'

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_compat_run_pip_2_test_empty_list_input.py F [100%]

=================================== FAILURES ===================================
___________________________ test_run_pip_empty_list ____________________________

    def test_run_pip_empty_list():
        with patch('httpie.manager.compat.run_pip', return_value=b'output'):
            result = run_pip([])
>           assert result == b'output'
E           assert b"\nUsage:   ...default: 5)\n" == b'output'
E             
E             At index 0 diff: b'\n' != b'o'
E             Use -v to get more diff

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_compat_run_pip_2_test_empty_list_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_compat_run_pip_2_test_empty_list_input.py::test_run_pip_empty_list
============================== 1 failed in 0.30s ===============================
"""