
import pytest
from isort._vendored.tomli._parser import NestedDict

def test_edge_cases():
    nd = NestedDict()
    
    # Test with None as a key
    with pytest.raises(KeyError):
        nd.get_or_create_nest(['a', 'b'], access_lists=False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        nd = NestedDict()
    
        # Test with None as a key
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_0_test_edge_cases.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.11s ===============================
"""