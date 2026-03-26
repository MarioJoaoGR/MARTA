
import pytest
from dataclasses import dataclass
from typing import Union
from dataclasses_json.mm import _UnionField

@dataclass
class Example:
    field: Union[int, str]

def test_invalid_input():
    desc = {Example: lambda v, a, d: None}
    union_field = _UnionField(desc, Example, 'field')
    
    value = {"__type": "str", "value": "test"}
    with pytest.warns(UserWarning):
        deserialized_value = union_field._deserialize(value, 'field', {'field': value})
        assert isinstance(deserialized_value, str)
        assert deserialized_value == "test"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        desc = {Example: lambda v, a, d: None}
        union_field = _UnionField(desc, Example, 'field')
    
        value = {"__type": "str", "value": "test"}
        with pytest.warns(UserWarning):
            deserialized_value = union_field._deserialize(value, 'field', {'field': value})
>           assert isinstance(deserialized_value, str)
E           assert False
E            +  where False = isinstance(None, str)

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_1_test_invalid_input.py:18: AssertionError

During handling of the above exception, another exception occurred:

    def test_invalid_input():
        desc = {Example: lambda v, a, d: None}
        union_field = _UnionField(desc, Example, 'field')
    
        value = {"__type": "str", "value": "test"}
>       with pytest.warns(UserWarning):
E       Failed: DID NOT WARN. No warnings of type (<class 'UserWarning'>,) were emitted.
E        Emitted warnings: [].

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_1_test_invalid_input.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__deserialize_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.04s ===============================

"""