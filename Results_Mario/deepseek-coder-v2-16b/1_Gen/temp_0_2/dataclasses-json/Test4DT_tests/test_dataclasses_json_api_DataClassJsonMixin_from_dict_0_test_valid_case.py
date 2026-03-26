
import pytest
from dataclasses import dataclass, fields
from datetime import datetime
from typing import Optional
from dataclasses_json.api import DataClassJsonMixin

@dataclass
class Person(DataClassJsonMixin):
    name: str
    age: int
    birth_date: datetime

def test_valid_case():
    person_dict = {'name': 'Alice', 'age': 30, 'birth_date': datetime(1992, 5, 20)}
    person = Person(**person_dict)
    
    assert person.name == 'Alice'
    assert person.age == 30
    assert person.birth_date == datetime(1992, 5, 20)
