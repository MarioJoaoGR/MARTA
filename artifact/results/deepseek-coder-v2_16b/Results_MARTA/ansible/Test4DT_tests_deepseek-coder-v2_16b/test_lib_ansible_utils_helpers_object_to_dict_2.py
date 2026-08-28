
import pytest
from ansible.utils.helpers import object_to_dict

# Test for None input

# Test for invalid exclude parameter type

# Test for valid object conversion without exclusion
def test_valid_object_no_exclusion():
    class Person:
        def __init__(self, name, age, city):
            self.name = name
            self.age = age
            self.city = city
    
    person = Person("Alice", 30, "Wonderland")
    expected_dict = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}
    assert object_to_dict(person) == expected_dict

# Test for valid object conversion with exclusion
def test_valid_object_with_exclusion():
    class Person:
        def __init__(self, name, age, city):
            self.name = name
            self.age = age
            self.city = city
    
    person = Person("Alice", 30, "Wonderland")
    expected_dict = {'name': 'Alice', 'age': 30}
    assert object_to_dict(person, exclude=["city"]) == expected_dict