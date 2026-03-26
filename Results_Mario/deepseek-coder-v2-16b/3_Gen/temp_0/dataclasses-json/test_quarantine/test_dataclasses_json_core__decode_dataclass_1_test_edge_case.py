
import pytest
from dataclasses import dataclass, fields
from dataclasses_json import dataclass_json
from typing import Type

@dataclass_json
@dataclass
class Person:
    name: str
    age: int = 0

def test_edge_case():
    person_data_none = None
    person_empty = '{}'
    
    with pytest.raises(TypeError):
        Person.from_dict(person_data_none)
    
    with pytest.raises(ValueError):
        Person.from_dict(eval(person_empty))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__decode_dataclass_1_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_1_test_edge_case.py:18:8: E1101: Class 'Person' has no 'from_dict' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_1_test_edge_case.py:21:8: E1101: Class 'Person' has no 'from_dict' member (no-member)


"""