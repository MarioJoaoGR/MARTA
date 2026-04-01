
from dataclasses_json.mm import _UnionField

def test_valid_inputs():
    union_field = _UnionField(desc="A description", cls=SomeClass, field="some_field")
    assert union_field.desc == "A description"
    assert union_field.cls is SomeClass
    assert union_field.field == "some_field"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField___init___0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___0_test_valid_inputs.py:5:56: E0602: Undefined variable 'SomeClass' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___0_test_valid_inputs.py:7:30: E0602: Undefined variable 'SomeClass' (undefined-variable)


"""