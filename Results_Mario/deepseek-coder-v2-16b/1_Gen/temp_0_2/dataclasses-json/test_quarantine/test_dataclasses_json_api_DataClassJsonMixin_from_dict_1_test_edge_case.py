
import pytest
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from typing import Type, Optional
from dataclasses_json.api import DataClassJsonMixin

@dataclass
class Person:
    name: str
    age: int
    birth_date: datetime

def test_edge_case():
    person_dict = {'name': 'Alice', 'age': 30, 'birth_date': '1992-05-20'}
    person = DataClassJsonMixin.from_dict(Person, person_dict)
    assert isinstance(person, Person)
    assert person.name == 'Alice'
    assert person.age == 30
    assert person.birth_date == datetime(1992, 5, 20)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_DataClassJsonMixin_from_dict_1_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_from_dict_1_test_edge_case.py:18:13: E1121: Too many positional arguments for classmethod call (too-many-function-args)


"""