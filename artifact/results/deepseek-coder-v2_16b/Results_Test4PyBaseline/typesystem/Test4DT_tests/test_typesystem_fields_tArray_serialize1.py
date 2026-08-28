
import pytest
from typesystem import Array, Field

# Test Case 1: Handling None input in serialize method
def test_serialize_none():
    array = Array(items=[Field()])
    assert array.serialize(None) is None, "Expected serialization of None to be None."

# Test Case 2: Serializing a list with valid items
def test_serialize_list():
    field1 = Field()
    field2 = Field()
    array = Array(items=[field1, field2])
    obj = [{"key1": "value1"}, {"key2": "value2"}]
    serialized = array.serialize(obj)
    assert isinstance(serialized, list), "Expected serialized result to be a list."
    assert len(serialized) == 2, "Expected the length of the serialized list to match the input list."