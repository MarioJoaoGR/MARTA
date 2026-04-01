
import pytest
from isort._vendored.tomli._parser import NestedDict

def test_get_or_create_nest():
    nd = NestedDict()
    
    # Test creating a new nest
    assert nd.get_or_create_nest(['a', 'b', 'c']) == {}
    assert nd.dict == {'a': {'b': {'c': {}}}}
    
    # Test accessing an existing nest
    nd.dict['a']['b']['c'] = {'d': 1}
    assert nd.get_or_create_nest(['a', 'b', 'c']) == {'d': 1}
    
    # Test raising KeyError when access_lists is False and a list is encountered
    with pytest.raises(KeyError):
        nd.get_or_create_nest(['a', 'list'], access_lists=False)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
___________________________ test_get_or_create_nest ____________________________

    def test_get_or_create_nest():
        nd = NestedDict()
    
        # Test creating a new nest
        assert nd.get_or_create_nest(['a', 'b', 'c']) == {}
        assert nd.dict == {'a': {'b': {'c': {}}}}
    
        # Test accessing an existing nest
        nd.dict['a']['b']['c'] = {'d': 1}
        assert nd.get_or_create_nest(['a', 'b', 'c']) == {'d': 1}
    
        # Test raising KeyError when access_lists is False and a list is encountered
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1_test_edge_case.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1_test_edge_case.py::test_get_or_create_nest
============================== 1 failed in 0.13s ===============================
"""