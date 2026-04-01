
from dataclasses_json.mm import inner as mm_inner
import warnings
from marshmallow import Schema, fields
from typing import Type, Dict, Any

def test_invalid_input_unknown_type():
    class MyType: pass
    
    schema = Schema()
    field = mm_inner(MyType, {})
    
    assert isinstance(field, fields.Field)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_inner_0_test_invalid_input_unknown_type
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_inner_0_test_invalid_input_unknown_type.py:2:0: E0611: No name 'inner' in module 'dataclasses_json.mm' (no-name-in-module)


"""