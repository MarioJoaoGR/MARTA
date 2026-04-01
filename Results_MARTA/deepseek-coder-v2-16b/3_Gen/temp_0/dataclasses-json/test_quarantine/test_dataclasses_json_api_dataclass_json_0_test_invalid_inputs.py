
import pytest
from dataclasses import dataclass
from typing import Optional, Type, Union
from enum import Enum
from dataclasses_json.api import dataclass_json

class LetterCase(Enum):
    CAMEL = "camel"
    SNAKE = "snake"
    PASCAL = "pascal"
    NONE = None

class Undefined(Enum):
    EXCLUDE = "exclude"

@dataclass
class Example:
    a: int
    b: str

def test_invalid_inputs():
    with pytest.raises(TypeError):
        @dataclass_json(letter_case=LetterCase.CAMEL)
        class InvalidExample:  # Missing field definition
            pass

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_invalid_inputs.py:23: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.07s ===============================
"""