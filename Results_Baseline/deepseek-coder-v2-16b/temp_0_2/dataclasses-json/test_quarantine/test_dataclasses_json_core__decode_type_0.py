
import pytest
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional
from dataclasses_json import DataClassJsonMixin

@dataclass
class ExampleDataClass(DataClassJsonMixin):
    date_field: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    amount: float = 0.0

def test_decode_type_with_missing_values():
    example_value = {"date_field": "2021-10-01", "amount": 12345.6789}
    with pytest.raises(TypeError):
        ExampleDataClass(**example_value)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0.py F [100%]

=================================== FAILURES ===================================
_____________________ test_decode_type_with_missing_values _____________________

    def test_decode_type_with_missing_values():
        example_value = {"date_field": "2021-10-01", "amount": 12345.6789}
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0.py::test_decode_type_with_missing_values
============================== 1 failed in 0.03s ===============================

"""