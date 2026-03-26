
import pytest
from dataclasses import dataclass
from dataclasses_json.undefined import _UndefinedParameterAction
from typing import Dict, Any

@dataclass
class Person:
    name: str
    age: int = 0

def test_handle_from_dict():
    kvs = {"name": "John Doe", "age": 30}
    result = _UndefinedParameterAction.handle_from_dict(Person, kvs)
    assert result == {'name': 'John Doe', 'age': 30}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction_handle_from_dict_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
____________________________ test_handle_from_dict _____________________________

    def test_handle_from_dict():
        kvs = {"name": "John Doe", "age": 30}
        result = _UndefinedParameterAction.handle_from_dict(Person, kvs)
>       assert result == {'name': 'John Doe', 'age': 30}
E       AssertionError: assert None == {'age': 30, 'name': 'John Doe'}

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction_handle_from_dict_0_test_edge_case.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction_handle_from_dict_0_test_edge_case.py::test_handle_from_dict
============================== 1 failed in 0.03s ===============================

"""