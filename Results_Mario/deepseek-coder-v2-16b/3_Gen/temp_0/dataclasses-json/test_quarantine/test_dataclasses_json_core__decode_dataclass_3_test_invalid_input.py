
import pytest
from dataclasses import dataclass, fields
from typing import get_type_hints
from dataclasses_json.core import _decode_dataclass

@pytest.fixture
def sample_dataclass():
    @dataclass
    class Person:
        name: str
        age: int = 0
    return Person

def test_invalid_input(sample_dataclass):
    with pytest.raises(TypeError):
        # Invalid input, should raise TypeError
        _decode_dataclass(sample_dataclass, {"name": "John Doe"}, True)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_3_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

sample_dataclass = <class 'Test4DT_tests.test_dataclasses_json_core__decode_dataclass_3_test_invalid_input.sample_dataclass.<locals>.Person'>

    def test_invalid_input(sample_dataclass):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_3_test_invalid_input.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_3_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.05s ===============================
"""