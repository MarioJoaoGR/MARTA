
import pytest
from dataclasses import dataclass, fields
from typing import Type, Optional, Any, Dict, TypeVar, get_type_hints
import json
from dataclasses_json.api import DataClassJsonMixin

# Define type variables
A = TypeVar('A', bound=DataClassJsonMixin)
JsonData = str

@dataclass
class Person(DataClassJsonMixin):
    name: str
    age: int

def test_invalid_input():
    with pytest.raises(TypeError):  # Expecting a TypeError because we are trying to instantiate an abstract base class
        DataClassJsonMixin()

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_json_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(TypeError):  # Expecting a TypeError because we are trying to instantiate an abstract base class
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_json_2_test_invalid_input.py:18: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_json_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================
"""