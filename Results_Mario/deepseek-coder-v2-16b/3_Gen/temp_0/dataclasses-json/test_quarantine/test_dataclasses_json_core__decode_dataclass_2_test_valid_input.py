
from dataclasses import fields, get_type_hints
from dataclasses_json.core import _decode_dataclass, _support_extended_types
import pytest
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID

@pytest.mark.parametrize("test_input, expected", [
    ({"name": "John Doe", "age": 30}, {"name": "John Doe", "age": 30}),
])
def test_valid_input(test_input, expected):
    class Person:
        def __init__(self, name: str, age: int = 0):
            self.name = name
            self.age = age

    # Test valid input with correct types
    result = _decode_dataclass(Person, test_input, infer_missing=False)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__decode_dataclass_2_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_2_test_valid_input.py:2:0: E0611: No name 'get_type_hints' in module 'dataclasses' (no-name-in-module)


"""