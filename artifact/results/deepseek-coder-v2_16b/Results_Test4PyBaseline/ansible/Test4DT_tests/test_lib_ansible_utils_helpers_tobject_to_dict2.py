
import pytest
from ansible.utils.helpers import object_to_dict

# Test cases for the object_to_dict function

def test_object_to_dict_with_none_exclude():
    class MyClass:
        def __init__(self):
            self.name = "John"
            self.age = 30
            self.id = 123

    obj = MyClass()
    result = object_to_dict(obj, exclude=None)
    assert result == {'name': 'John', 'age': 30, 'id': 123}

def test_object_to_dict_with_empty_exclude():
    class MyClass:
        def __init__(self):
            self.name = "John"
            self.age = 30
            self.id = 123

    obj = MyClass()
    result = object_to_dict(obj, exclude=[])