
import pytest
from ansible.utils.helpers import object_to_dict

# Test case for valid input object
def test_valid_input():
    class Person:
        def __init__(self, name, age, city):
            self.name = name
            self.age = age
            self.city = city
    
    person = Person("Alice", 30, "Wonderland")
    expected_dict = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}
    result_dict = object_to_dict(person)
    assert result_dict == expected_dict

# Test case for invalid input (None)

# Test case for excluding specific attributes
def test_exclude_attributes():
    class Person:
        def __init__(self, name, age, city):
            self.name = name
            self.age = age
            self.city = city
    
    person = Person("Alice", 30, "Wonderland")
    expected_dict = {'name': 'Alice', 'age': 30}
    result_dict = object_to_dict(person, exclude=["city"])
    assert result_dict == expected_dict