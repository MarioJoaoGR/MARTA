
import pytest
from httpie.cli.dicts import MultiValueOrderedDict

def test_valid_inputs():
    mvod = MultiValueOrderedDict()
    
    # Test setting a single value for a new key
    mvod['foo'] = 'bar'
    assert mvod['foo'] == ['bar']

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_dicts_MultiValueOrderedDict___setitem___1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        mvod = MultiValueOrderedDict()
    
        # Test setting a single value for a new key
        mvod['foo'] = 'bar'
>       assert mvod['foo'] == ['bar']
E       AssertionError: assert 'bar' == ['bar']

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_dicts_MultiValueOrderedDict___setitem___1_test_valid_inputs.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_dicts_MultiValueOrderedDict___setitem___1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================
"""