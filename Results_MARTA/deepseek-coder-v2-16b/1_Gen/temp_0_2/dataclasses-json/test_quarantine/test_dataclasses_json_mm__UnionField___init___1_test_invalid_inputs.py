
import pytest
from dataclasses_json import mm  # Assuming this is the correct module to import from

def test_invalid_inputs():
    with pytest.raises(TypeError):
        union_field = _UnionField(desc="A description", cls=SomeClass, field="some_field")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField___init___1_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___1_test_invalid_inputs.py:7:22: E0602: Undefined variable '_UnionField' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___1_test_invalid_inputs.py:7:60: E0602: Undefined variable 'SomeClass' (undefined-variable)


"""