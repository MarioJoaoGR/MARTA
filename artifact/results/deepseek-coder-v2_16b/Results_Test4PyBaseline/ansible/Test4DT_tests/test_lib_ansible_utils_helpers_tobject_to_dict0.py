
import pytest
from ansible.utils.helpers import object_to_dict

# Test cases for the object_to_dict function

def test_basic_usage():
    class MyClass:
        def __init__(self):
            self.name = "John"
            self.age = 30
            self.id = 123

    obj = MyClass()
    result = object_to_dict(obj, exclude=['id'])
    assert result == {'name': 'John', 'age': 30}

def test_no_exclusion():
    class AnotherClass:
        def __init__(self):
            self.attr1 = "value1"
            self.attr2 = "value2"
            self.attr3 = "value3"

    obj = AnotherClass()
    result = object_to_dict(obj)
    assert result == {'attr1': 'value1', 'attr2': 'value2', 'attr3': 'value3'}

def test_excluding_multiple_keys():
    class YetAnotherClass:
        def __init__(self):
            self.key1 = "val1"
            self.key2 = "val2"
            self.key3 = "val3"
            self.key4 = "val4"

    obj = YetAnotherClass()
    result = object_to_dict(obj, exclude=['key2', 'key4'])
    assert result == {'key1': 'val1', 'key3': 'val3'}

def test_custom_object():
    class CustomObject:
        def __init__(self):
            self.field1 = "alpha"
            self.field2 = "beta"
            self.field3 = "gamma"

    obj = CustomObject()
    result = object_to_dict(obj)
    assert result == {'field1': 'alpha', 'field2': 'beta', 'field3': 'gamma'}

def test_using_dictionary():
    obj_dict = {"key1": "value1", "key2": "value2"}
    result = object_to_dict(obj_dict, exclude=['key2'])
    assert result == {'key1': 'value1'}
