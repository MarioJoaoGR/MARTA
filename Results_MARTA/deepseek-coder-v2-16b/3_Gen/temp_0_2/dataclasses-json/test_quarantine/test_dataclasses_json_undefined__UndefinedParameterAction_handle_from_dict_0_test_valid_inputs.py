
import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Dict, Any
from dataclasses_json.undefined import _UndefinedParameterAction

@dataclass
class MyClass:
    param1: int
    param2: str

def test_valid_inputs():
    my_dict = {'param1': 1, 'param2': 'value'}
    result = _UndefinedParameterAction.handle_from_dict(MyClass, my_dict)
    assert result == {'param1': 1, 'param2': 'value'}, f"Expected {my_dict}, but got {result}"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction_handle_from_dict_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        my_dict = {'param1': 1, 'param2': 'value'}
        result = _UndefinedParameterAction.handle_from_dict(MyClass, my_dict)
>       assert result == {'param1': 1, 'param2': 'value'}, f"Expected {my_dict}, but got {result}"
E       AssertionError: Expected {'param1': 1, 'param2': 'value'}, but got None
E       assert None == {'param1': 1, 'param2': 'value'}

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction_handle_from_dict_0_test_valid_inputs.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__UndefinedParameterAction_handle_from_dict_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.03s ===============================
"""