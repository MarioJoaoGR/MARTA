
import pytest
from dataclasses import dataclass, fields
from typing import Type, Dict, Any
from dataclasses_json.core import _decode_dataclass

@pytest.fixture
def example_dataclass():
    @dataclass
    class Example:
        a: int
        b: str
    
    return Example(a=1, b="test")

def test_valid_inputs(example_dataclass):
    json_str = '{"a": 1, "b": "test"}'
    result = _decode_dataclass(type(example_dataclass), json.loads(json_str), False)
    
    assert isinstance(result, type(example_dataclass))
    assert result.a == example_dataclass.a
    assert result.b == example_dataclass.b

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__decode_dataclass_1_test_valid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_1_test_valid_inputs.py:18:56: E0602: Undefined variable 'json' (undefined-variable)


"""