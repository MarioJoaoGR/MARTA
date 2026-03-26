
import pytest
from dataclasses import dataclass
from typing import List, Optional, Union, Dict, Any, Enum
from dataclasses_json.core import _decode_generic

@dataclass
class Person:
    name: str
    age: int

def test_error_case():
    person_data = {"name": "John Doe", "age": 30}
    decoded_person = _decode_generic(Person, person_data, infer_missing=False)
    assert decoded_person.name == "John Doe"
    assert decoded_person.age == 30

    list_of_numbers = [1, 2, 3]
    decoded_list = _decode_generic(List[int], list_of_numbers, infer_missing=False)
    assert decoded_list == [1, 2, 3]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__decode_generic_4_test_error_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_generic_4_test_error_case.py:4:0: E0611: No name 'Enum' in module 'typing' (no-name-in-module)


"""