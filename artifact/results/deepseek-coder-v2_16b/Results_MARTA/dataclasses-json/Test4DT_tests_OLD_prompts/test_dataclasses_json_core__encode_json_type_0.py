
import pytest
from dataclasses_json.core import _encode_json_type, Json, _ExtendedEncoder

# Test encoding an integer
def test__encode_json_type_integer():
    assert _encode_json_type(42) == 42

# Test encoding a string
def test__encode_json_type_string():
    assert _encode_json_type("hello") == "hello"

# Test encoding a list
def test__encode_json_type_list():
    assert _encode_json_type([1, 2, 3]) == [1, 2, 3]

# Test encoding a dictionary
def test__encode_json_type_dict():
    assert _encode_json_type({"key": "value"}) == {"key": "value"}

# Test encoding a complex object using the default encoder
class ComplexObject:
    def __init__(self, value):
        self.value = value

def test__encode_json_type_complex_object():
    obj = ComplexObject("complex_value")
    with pytest.raises(TypeError) as excinfo:
        _encode_json_type(obj)
    assert str(excinfo.value) == 'Object of type ComplexObject is not JSON serializable'
