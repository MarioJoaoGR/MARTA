
import pytest
from isort._vendored.tomli._parser import NestedDict

# Test cases for NestedDict class methods

def test_get_or_create_nest():
    nd = NestedDict()
    assert nd.dict == {}
    
    # Accessing a non-existent nested structure should raise KeyError
    with pytest.raises(KeyError):
        nd.get_or_create_nest(['non', 'existent', 'keys'])
    
    # Creating a nested structure
    nd.get_or_create_nest(['a', 'b', 'c'])
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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_append_nest_to_list_0.py F [100%]

=================================== FAILURES ===================================
___________________________ test_get_or_create_nest ____________________________

    def test_get_or_create_nest():
        nd = NestedDict()
        assert nd.dict == {}
    
        # Accessing a non-existent nested structure should raise KeyError
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_append_nest_to_list_0.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_append_nest_to_list_0.py::test_get_or_create_nest
============================== 1 failed in 0.10s ===============================
"""