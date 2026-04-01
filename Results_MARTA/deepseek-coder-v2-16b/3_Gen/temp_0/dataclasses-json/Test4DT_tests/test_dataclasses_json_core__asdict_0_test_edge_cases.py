
import pytest
from dataclasses import dataclass, fields
from typing import List, Dict, Union, Collection, Mapping
import copy
from dataclasses_json.core import _asdict

# Assuming this is your module where the function `_asdict` resides
# from your_module import MyDataClass, _asdict

@dataclass
class MyDataClass:
    name: str
    age: int

def test_asdict_basic():
    @dataclass
    class TestDataClass:
        a: int
        b: str
    
    obj = TestDataClass(a=1, b="test")
    result = _asdict(obj)
    assert isinstance(result, dict)
    assert result == {'a': 1, 'b': 'test'}

def test_asdict_nested():
    @dataclass
    class NestedDataClass:
        nested: MyDataClass
    
    obj = NestedDataClass(nested=MyDataClass(name="John", age=30))
    result = _asdict(obj)
    assert isinstance(result, dict)
    assert result == {'nested': {'name': 'John', 'age': 30}}

def test_asdict_encode_json():
    @dataclass
    class EncodeDataClass:
        value: Union[int, str]
    
    obj = EncodeDataClass(value=123)
    result = _asdict(obj, encode_json=True)
    assert isinstance(result, dict)
    assert result == {'value': 123}

def test_asdict_collection():
    @dataclass
    class CollectionDataClass:
        values: List[int]
    
    obj = CollectionDataClass(values=[1, 2, 3])
    result = _asdict(obj)
    assert isinstance(result, dict)
    assert result == {'values': [1, 2, 3]}

def test_asdict_mapping():
    @dataclass
    class MappingDataClass:
        mapping: Dict[str, int]
    
    obj = MappingDataClass(mapping={"key1": 1, "key2": 2})
    result = _asdict(obj)
    assert isinstance(result, dict)
    assert result == {'mapping': {"key1": 1, "key2": 2}}

def test_asdict_no_encode():
    @dataclass
    class NoEncodeDataClass:
        value: int
    
    obj = NoEncodeDataClass(value=456)
    result = _asdict(obj)
    assert isinstance(result, dict)
    assert result == {'value': 456}
