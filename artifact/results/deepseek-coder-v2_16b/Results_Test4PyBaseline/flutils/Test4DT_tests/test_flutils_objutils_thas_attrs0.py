
import pytest
from flutils.objutils import has_attrs

# Test cases for has_attrs function

def test_has_all_attributes():
    obj = {}  # Replace with any other object type or instance as needed
    attrs = ['get', 'keys', 'items', 'values']
    result = has_attrs(obj, *attrs)
    assert result is True, "Expected True because the dictionary should have all specified attributes"

def test_does_not_have_attributes():
    obj = dict()  # Using a dictionary as an example
    attrs = ['non_existent_attr1', 'non_existent_attr2']
    result = has_attrs(obj, *attrs)
    assert result is False, "Expected False because the dictionary does not have non-existent attributes"

def test_custom_object_attributes():
    class CustomObj:
        def __init__(self):
            self.attr1 = 'value1'
            self.attr2 = 'value2'

    obj = CustomObj()  # Replace with your custom object instance
    attrs = ['attr1', 'attr2']
    result = has_attrs(obj, *attrs)
    assert result is True, "Expected True because the custom object should have all specified attributes"

def test_string_attributes():
    obj = "example"  # Using a string as an example
    attrs = ['upper', 'lower', 'split']
    result = has_attrs(obj, *attrs)