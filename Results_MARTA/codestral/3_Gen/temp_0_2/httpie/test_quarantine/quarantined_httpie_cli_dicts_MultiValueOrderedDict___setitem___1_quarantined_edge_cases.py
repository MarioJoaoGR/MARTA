
import pytest
from httpie.cli.dicts import MultiValueOrderedDict

def test_edge_cases():
    mvod = MultiValueOrderedDict()
    
    # Test setting a single value for the first time
    mvod['key1'] = 'value1'
    assert mvod['key1'] == ['value1']

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

httpie/Test4DT_tests_codestral/test_httpie_cli_dicts_MultiValueOrderedDict___setitem___1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        mvod = MultiValueOrderedDict()
    
        # Test setting a single value for the first time
        mvod['key1'] = 'value1'
>       assert mvod['key1'] == ['value1']
E       AssertionError: assert 'value1' == ['value1']

httpie/Test4DT_tests_codestral/test_httpie_cli_dicts_MultiValueOrderedDict___setitem___1_test_edge_cases.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_cli_dicts_MultiValueOrderedDict___setitem___1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.11s ===============================
"""