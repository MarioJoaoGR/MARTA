
import pytest
from isort._vendored.tomli._parser import NestedDict  # Correct module path

def test_get_or_create_nest():
    nd = NestedDict()
    
    # Test getting or creating a nested dictionary
    result = nd.get_or_create_nest(['a', 'b', 'c'])
    assert isinstance(result, dict), "Expected a dictionary"
    assert result == {}, "Expected an empty dictionary for new nest"
    
    # Modify the structure to check if it returns existing nested dictionary
    nd.dict['a'] = {'b': {}}
    result = nd.get_or_create_nest(['a', 'b', 'c'])
    assert isinstance(result, dict), "Expected a dictionary"
    assert result == {}, "Expected an empty dictionary for existing nest"
    
    # Test accessing elements in a list context
    nd.dict['x'] = [1, 2, 3]
    result = nd.get_or_create_nest(['x'], access_lists=False)
    assert result == 3, "Expected the last element of the list"
    
    # Test raising KeyError when accessing a non-existing key sequence
    with pytest.raises(KeyError):
        nd.get_or_create_nest(['non', 'existent', 'keys'])

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_2_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
___________________________ test_get_or_create_nest ____________________________

    def test_get_or_create_nest():
        nd = NestedDict()
    
        # Test getting or creating a nested dictionary
        result = nd.get_or_create_nest(['a', 'b', 'c'])
        assert isinstance(result, dict), "Expected a dictionary"
        assert result == {}, "Expected an empty dictionary for new nest"
    
        # Modify the structure to check if it returns existing nested dictionary
        nd.dict['a'] = {'b': {}}
        result = nd.get_or_create_nest(['a', 'b', 'c'])
        assert isinstance(result, dict), "Expected a dictionary"
        assert result == {}, "Expected an empty dictionary for existing nest"
    
        # Test accessing elements in a list context
        nd.dict['x'] = [1, 2, 3]
>       result = nd.get_or_create_nest(['x'], access_lists=False)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_2_test_edge_cases.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <isort._vendored.tomli._parser.NestedDict object at 0x7f659f926c10>
key = ['x']

    def get_or_create_nest(
        self,
        key: Key,
        *,
        access_lists: bool = True,
    ) -> dict:
        cont: Any = self.dict
        for k in key:
            if k not in cont:
                cont[k] = {}
            cont = cont[k]
            if access_lists and isinstance(cont, list):
                cont = cont[-1]
            if not isinstance(cont, dict):
>               raise KeyError("There is no nest behind this key")
E               KeyError: 'There is no nest behind this key'

isort/isort/_vendored/tomli/_parser.py:212: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_2_test_edge_cases.py::test_get_or_create_nest
============================== 1 failed in 0.14s ===============================
"""