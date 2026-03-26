
import pytest
from typing import Any, Dict, List, Union
from isort._vendored.tomli._parser import NestedDict

# Define the type for the keys in the dictionary
Key = List[Union[str, int]]

def test_get_or_create_nest_access_list():
    nd = NestedDict()
    nd.dict = {'a': {'b': {'c': [1, 2, 3]}}}
    result = nd.get_or_create_nest(['a', 'b', 'c', 0])
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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1.py F [100%]

=================================== FAILURES ===================================
_____________________ test_get_or_create_nest_access_list ______________________

    def test_get_or_create_nest_access_list():
        nd = NestedDict()
        nd.dict = {'a': {'b': {'c': [1, 2, 3]}}}
>       result = nd.get_or_create_nest(['a', 'b', 'c', 0])

isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <isort._vendored.tomli._parser.NestedDict object at 0x7fc67dd1be10>
key = ['a', 'b', 'c', 0]

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
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_NestedDict_get_or_create_nest_1.py::test_get_or_create_nest_access_list
============================== 1 failed in 0.10s ===============================
"""