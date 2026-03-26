
from dataclasses import dataclass
from typing import Dict, Optional
from dataclasses_json import api as dcj_api  # Assuming this is the correct module path

# Define a simple dataclass for testing
@dataclass
class Person:
    name: str
    age: int

# Ensure that DataClassJsonMixin has the to_dict method defined
def test_valid_case():
    @dataclass
    class PersonWithToDict(dcj_api.DataClassJsonMixin):
        name: str
        age: int
    
    person = PersonWithToDict(name="John", age=30)
    assert isinstance(person, dcj_api.DataClassJsonMixin)
    result = person.to_dict()
    expected = {'name': 'John', 'age': 30}
    assert result == expected
