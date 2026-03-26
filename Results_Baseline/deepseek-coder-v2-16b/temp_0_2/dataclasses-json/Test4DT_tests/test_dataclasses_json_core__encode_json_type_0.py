# Module: dataclasses_json.core
import pytest
from dataclasses_json.core import _encode_json_type, _ExtendedEncoder
from json import JSONEncoder

# Define a mock encoder class to simulate the behavior of _ExtendedEncoder
class MockEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, list):
            return [_encode_json_type(i) for i in obj]
        elif isinstance(obj, dict):
            return {k: _encode_json_type(v) for k, v in obj.items()}
        else:
            return super().default(obj)

# Test cases for _encode_json_type function
def test_encode_json_type_list():
    value = [1, {"key": "value"}, ["nested", 2]]
    encoded_value = _encode_json_type(value, default=MockEncoder().default)
    assert encoded_value == [1, {'key': 'value'}, ['nested', 2]]

def test_encode_json_type_dict():
    value = {"list": [1, 2, 3], "dict": {"a": "b"}}
    encoded_value = _encode_json_type(value, default=MockEncoder().default)
    assert encoded_value == {"list": [1, 2, 3], "dict": {"a": "b"}}

def test_encode_json_type_non_json():
    value = None
    encoded_value = _encode_json_type(value, default=MockEncoder().default)
    assert encoded_value == None

def test_encode_json_type_custom_encoder():
    class CustomEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj, list):
                return [_encode_json_type(i) for i in obj]
            elif isinstance(obj, dict):
                return {k: _encode_json_type(v) for k, v in obj.items()}
            else:
                return super().default(obj)
    value = [1, {"key": "value"}, ["nested", 2]]
    encoded_value = _encode_json_type(value, default=CustomEncoder().default)
    assert encoded_value == [1, {'key': 'value'}, ['nested', 2]]

if __name__ == "__main__":
    pytest.main()
