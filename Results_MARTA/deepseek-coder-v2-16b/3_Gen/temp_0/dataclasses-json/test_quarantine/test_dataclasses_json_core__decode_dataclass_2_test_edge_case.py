
import pytest
from dataclasses import dataclass, fields
from dataclasses_json import dataclass_json
from typing import Optional

@dataclass_json
@dataclass
class Person:
    name: str
    age: int = 0

def test_edge_case():
    # Test with None input
    person_none = Person.from_dict(None)
    assert isinstance(person_none, Person) and person_none.name is None and person_none.age == 0
    
    # Test with empty dictionary
    person_empty = Person.from_dict({})
    assert isinstance(person_empty, Person) and person_empty.name is None and person_empty.age == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__decode_dataclass_2_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_2_test_edge_case.py:15:18: E1101: Class 'Person' has no 'from_dict' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_2_test_edge_case.py:19:19: E1101: Class 'Person' has no 'from_dict' member (no-member)


"""