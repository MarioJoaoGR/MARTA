
from dataclasses import dataclass
import pytest
from dataclasses_json.mm import _UnionField

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Missing 'desc' parameter
        _UnionField(cls=type, field="my_field")

    with pytest.raises(TypeError):
        # Missing 'cls' parameter
        _UnionField(desc="A description", field="my_field")

    with pytest.raises(TypeError):
        # Missing 'field' parameter
        _UnionField(desc="A description", cls=type)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField___init___1_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___1_test_invalid_inputs.py:9:8: E1120: No value for argument 'desc' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___1_test_invalid_inputs.py:13:8: E1120: No value for argument 'cls' in constructor call (no-value-for-parameter)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___1_test_invalid_inputs.py:17:8: E1120: No value for argument 'field' in constructor call (no-value-for-parameter)


"""