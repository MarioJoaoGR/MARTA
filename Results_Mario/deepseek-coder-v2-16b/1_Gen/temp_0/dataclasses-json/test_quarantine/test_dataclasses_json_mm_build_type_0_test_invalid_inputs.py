
import pytest
from dataclasses import dataclass, fields as dataclass_fields
from marshmallow import Schema, fields
from typing import List, Optional, Union
from dataclasses_json.mm import build_type

@dataclass
class MyModel:
    name: str
    age: int

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test case for invalid type input (not a valid Python type)
        build_type(None, {}, None, dataclass_fields['name'], MyModel)
        
    with pytest.raises(TypeError):
        # Test case for invalid options input (options should be a dictionary)
        build_type(MyModel, "invalid", None, dataclass_fields['age'], MyModel)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_build_type_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_invalid_inputs.py:16:35: E1136: Value 'dataclass_fields' is unsubscriptable (unsubscriptable-object)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_type_0_test_invalid_inputs.py:20:45: E1136: Value 'dataclass_fields' is unsubscriptable (unsubscriptable-object)

"""