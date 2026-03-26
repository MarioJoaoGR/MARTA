
import pytest
from dataclasses import dataclass
from typing import Union
from dataclasses_json.mm import _UnionField, _issubclass_safe, is_dataclass, _get_type_origin

@dataclass
class Example:
    value: Union[int, float]

def test_valid_input():
    desc = {
        int: ...,  # Mock serialization schema for int
        float: ...  # Mock serialization schema for float
    }
    
    union_field = _UnionField(desc, Example, Example.value)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        desc = {
            int: ...,  # Mock serialization schema for int
            float: ...  # Mock serialization schema for float
        }
    
>       union_field = _UnionField(desc, Example, Example.value)
E       AttributeError: type object 'Example' has no attribute 'value'

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_valid_input.py:17: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""