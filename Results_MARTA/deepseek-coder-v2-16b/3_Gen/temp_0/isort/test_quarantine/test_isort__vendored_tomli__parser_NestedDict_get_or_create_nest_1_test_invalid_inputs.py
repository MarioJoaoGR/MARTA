
import pytest
from isort._vendored.tomli._parser import NestedDict

def test_invalid_inputs():
    nd = NestedDict()
    
    # Test with a non-existent key sequence
    with pytest.raises(KeyError) as excinfo:
        nd.get_or_create_nest(['non', 'existent', 'keys'])
        
    assert isinstance(excinfo.value, KeyError), "Expected KeyError but got something else"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        nd = NestedDict()
    
        # Test with a non-existent key sequence
>       with pytest.raises(KeyError) as excinfo:
E       Failed: DID NOT RAISE <class 'KeyError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1_test_invalid_inputs.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.12s ===============================
"""