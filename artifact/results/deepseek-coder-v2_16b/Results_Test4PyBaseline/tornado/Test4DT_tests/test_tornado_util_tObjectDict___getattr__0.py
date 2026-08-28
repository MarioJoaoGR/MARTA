
import pytest
from tornado.util import ObjectDict

# Test creating an instance of ObjectDict
def test_create_instance():
    obj = ObjectDict()
    assert isinstance(obj, ObjectDict), "Instance should be a type of ObjectDict"

# Test setting and getting attributes dynamically
def test_set_and_get_attributes():
    obj = ObjectDict()
    obj.name = 'Alice'
    obj.age = 30
    assert obj.name == 'Alice', "Attribute name should be set to 'Alice'"
    assert obj.age == 30, "Attribute age should be set to 30"

# Test accessing a non-existent attribute
def test_access_non_existent_attribute():
    obj = ObjectDict({'name': 'Alice'})
    with pytest.raises(AttributeError) as e:
        print(obj.age)