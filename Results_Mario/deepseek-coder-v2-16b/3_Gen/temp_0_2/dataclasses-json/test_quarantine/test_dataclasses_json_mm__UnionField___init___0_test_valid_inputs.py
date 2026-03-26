
import pytest
from dataclasses_json import _UnionField

def test_valid_inputs():
    # Test valid inputs for _UnionField initialization
    desc = "A union field"
    cls = type('RecordClass', (), {})
    field = 'data'
    
    union_field = _UnionField(desc, cls, field)
    
    assert union_field.desc == desc
    assert union_field.cls is cls
    assert union_field.field == field

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField___init___0_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField___init___0_test_valid_inputs.py:3:0: E0611: No name '_UnionField' in module 'dataclasses_json' (no-name-in-module)


"""