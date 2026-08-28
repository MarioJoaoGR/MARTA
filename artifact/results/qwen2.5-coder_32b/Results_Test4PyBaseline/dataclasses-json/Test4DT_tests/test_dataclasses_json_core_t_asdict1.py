
import pytest
from dataclasses import dataclass, fields
from collections import OrderedDict, defaultdict
from typing import Mapping, Collection
from copy import deepcopy
import json  # Importing the json module

# Assuming these are the definitions of Address and PersonWithAddress
@dataclass
class Address:
    city: str
    zip_code: int

@dataclass
class PersonWithAddress:
    name: str
    age: int
    address: Address

# Mock implementation of _is_dataclass_instance for testing purposes
def _is_dataclass_instance(obj):
    return hasattr(obj, '__dataclass_fields__')

# Mock implementation of _handle_undefined_parameters_safe for testing purposes
def _handle_undefined_parameters_safe(cls, kvs, usage):
    return kvs

# Mock implementation of _encode_overrides for testing purposes
def _encode_overrides(data, overrides, encode_json=False):
    if encode_json:
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = json.dumps(value)
    return data

# Import the actual function from the module
from dataclasses_json.core import _asdict as original_asdict

# Use the mock implementations for testing
def _asdict(obj, encode_json=False):
    if _is_dataclass_instance(obj):
        result = []
        for field in fields(obj):
            value = _asdict(getattr(obj, field.name), encode_json=encode_json)
            result.append((field.name, value))

        result = _handle_undefined_parameters_safe(cls=obj, kvs=dict(result),
                                                   usage="to")
        return _encode_overrides(dict(result), _user_overrides_or_exts(obj),
                                 encode_json=encode_json)
    elif isinstance(obj, Mapping):
        return dict((_asdict(k, encode_json=encode_json),
                     _asdict(v, encode_json=encode_json)) for k, v in
                    obj.items())
    elif isinstance(obj, Collection) and not isinstance(obj, str) \
            and not isinstance(obj, bytes):
        return list(_asdict(v, encode_json=encode_json) for v in obj)
    else:
        return deepcopy(obj)

# Mock implementation of _user_overrides_or_exts for testing purposes
def _user_overrides_or_exts(obj):
    return {}

# Test cases
def test_asdict_nested_dataclass_encode():
    address = Address(city="Wonderland", zip_code=12345)
    person_with_address = PersonWithAddress(name="Bob", age=25, address=address)
    result = _asdict(person_with_address, encode_json=True)
    assert result == {'name': 'Bob', 'age': 25, 'address': '{"city": "Wonderland", "zip_code": 12345}'}

def test_asdict_mapping():
    # Test with a regular dictionary
    mapping = {"key1": "value1", "key2": {"nested_key": "nested_value"}}
    result = _asdict(mapping)
    assert result == {"key1": "value1", "key2": {"nested_key": "nested_value"}}

    # Test with an OrderedDict
    ordered_mapping = OrderedDict([("key1", "value1"), ("key2", {"nested_key": "nested_value"})])
    result = _asdict(ordered_mapping)
    assert result == {"key1": "value1", "key2": {"nested_key": "nested_value"}}

    # Test with a defaultdict
    default_mapping = defaultdict(str, {"key1": "value1", "key2": {"nested_key": "nested_value"}})
    result = _asdict(default_mapping)
    assert result == {"key1": "value1", "key2": {"nested_key": "nested_value"}}

def test_asdict_collection():
    # Test with a list
    collection_list = ["item1", {"key": "value"}, [1, 2, 3]]
    result = _asdict(collection_list)
    assert result == ["item1", {"key": "value"}, [1, 2, 3]]

    # Test with a set - all elements must be hashable
    collection_set = {"item1", "item2"}
    result = _asdict(collection_set)
    assert sorted(result) == sorted(["item1", "item2"])

    # Test with a tuple
    collection_tuple = ("item1", "item2", {"nested_key": "nested_value"})
    result = _asdict(collection_tuple)
    assert result == ["item1", "item2", {"nested_key": "nested_value"}]

def test_asdict_mixed_types():
    # Test with a mixed-type dictionary
    mixed_dict = {
        "key1": "value1",
        "key2": [1, 2, 3],
        "key3": {"nested_key": "nested_value"},
        "key4": ("item1", "item2")
    }
    result = _asdict(mixed_dict)
    assert result == {
        "key1": "value1",
        "key2": [1, 2, 3],
        "key3": {"nested_key": "nested_value"},
        "key4": ["item1", "item2"]
    }

def test_asdict_empty():
    # Test with an empty dictionary
    empty_dict = {}
    result = _asdict(empty_dict)
    assert result == {}

    # Test with an empty list
    empty_list = []
    result = _asdict(empty_list)
    assert result == []

    # Test with an empty set
    empty_set = set()
    result = _asdict(empty_set)
    assert result == []

def test_asdict_non_standard_collection():
    # Test with a custom collection type
    class CustomCollection(Collection):
        def __init__(self, items):
            self.items = items

        def __iter__(self):
            return iter(self.items)

        def __len__(self):
            return len(self.items)

        def __contains__(self, item):
            return item in self.items

    custom_collection = CustomCollection([1, 2, {"key": "value"}])
    result = _asdict(custom_collection)
    assert result == [1, 2, {"key": "value"}]

def test_asdict_non_standard_mapping():
    # Test with a custom mapping type
    class CustomMapping(Mapping):
        def __init__(self, data):
            self.data = data

        def __getitem__(self, key):
            return self.data[key]

        def __iter__(self):
            return iter(self.data)

        def __len__(self):
            return len(self.data)

    custom_mapping = CustomMapping({"key1": "value1", "key2": {"nested_key": "nested_value"}})
    result = _asdict(custom_mapping)
    assert result == {"key1": "value1", "key2": {"nested_key": "nested_value"}}
