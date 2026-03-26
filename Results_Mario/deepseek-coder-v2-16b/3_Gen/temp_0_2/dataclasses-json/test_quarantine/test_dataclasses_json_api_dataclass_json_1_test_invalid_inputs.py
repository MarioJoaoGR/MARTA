
from dataclasses import dataclass, fields
from typing import Optional, Type, Union
from pytest import raises
from dataclasses_json.api import dataclass_json

@dataclass_json
@dataclass
class Example:
    name: str
    age: int

def test_invalid_inputs():
    with raises(TypeError):  # Expect a TypeError for missing arguments
        @dataclass_json
        @dataclass
        class InvalidExample:
            pass
    
    with raises(TypeError):  # Expect a TypeError for incomplete dataclass definition
        @dataclass_json
        @dataclass
        class IncompleteExample:
            name: str

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with raises(TypeError):  # Expect a TypeError for missing arguments
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_1_test_invalid_inputs.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.03s ===============================
"""