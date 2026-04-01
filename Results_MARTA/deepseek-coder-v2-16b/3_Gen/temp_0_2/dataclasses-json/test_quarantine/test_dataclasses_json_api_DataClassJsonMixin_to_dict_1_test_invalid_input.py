
from dataclasses import dataclass
from typing import Dict, Optional
from dataclasses_json import DataClassJsonMixin
import pytest

@dataclass
class Person(DataClassJsonMixin):
    name: str
    age: int

def test_invalid_input():
    with pytest.raises(AttributeError):
        person = Person(name="John", age=30)
        person.to_dict()  # This should raise an AttributeError because to_dict is not defined in the base class DataClassJsonMixin

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_to_dict_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_to_dict_1_test_invalid_input.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_to_dict_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================
"""