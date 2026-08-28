
import pytest
from ansible.utils.helpers import object_to_dict

# Test case for valid input
def test_valid_object():
    class Person:
        def __init__(self, name, age, city):
            self.name = name
            self.age = age
            self.city = city

    person = Person("Alice", 30, "Wonderland")
    result = object_to_dict(person)
    assert isinstance(result, dict), "Expected a dictionary"
    assert set(result.keys()) == {'name', 'age', 'city'}, "Keys do not match expected keys"
    assert result == {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}

# Test case for invalid input (should raise TypeError)