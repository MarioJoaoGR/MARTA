
import pytest
from dataclasses import dataclass
from typing import Optional, Union, Tuple, Callable
from dataclasses_json import DataClassJsonMixin
import json

@dataclass
class Person(DataClassJsonMixin):
    name: str
    age: int

def test_error_case():
    person = Person(name="John", age=30)
    with pytest.raises(AttributeError):
        # This should raise an AttributeError because DataClassJsonMixin does not have a to_json method directly
        assert person.to_json() == '{"name": "John", "age": 30}'

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_to_json_1_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        person = Person(name="John", age=30)
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_to_json_1_test_error_case.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_to_json_1_test_error_case.py::test_error_case
============================== 1 failed in 0.04s ===============================
"""