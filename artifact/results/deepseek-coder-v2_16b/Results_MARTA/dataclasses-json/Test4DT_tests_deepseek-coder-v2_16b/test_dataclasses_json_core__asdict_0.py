
import pytest
from dataclasses_json.core import _asdict
from dataclasses import dataclass, fields
from typing import Dict, Optional, Collection, Mapping
import copy

@dataclass
class MyDataClass:
    name: str
    age: int
    dataclass_json_config: Optional[Dict] = None


@dataclass
class CustomClass:
    value: str


def test_custom_class_instance():
    custom_obj = CustomClass(value="example")
    result = _asdict(custom_obj)
    assert isinstance(result, dict)
    assert result['value'] == 'example'

@dataclass
class NestedDataClass:
    inner: MyDataClass

def test_nested_data_class():
    nested_obj = NestedDataClass(inner=MyDataClass(name='John', age=30))
    result = _asdict(nested_obj)
    assert isinstance(result, dict)
    assert result['inner']['name'] == 'John'
    assert result['inner']['age'] == 30

@dataclass
class MappingDataClass:
    name: str
    age: int
    config: Dict

def test_mapping_instance():
    mapping_obj = MappingDataClass(name='Jane', age=25, config={'key': 'value'})
    result = _asdict(mapping_obj)
    assert isinstance(result, dict)
    assert result['name'] == 'Jane'
    assert result['age'] == 25
    assert result['config']['key'] == 'value'

@dataclass
class CollectionDataClass:
    values: list

def test_collection_instance():
    collection_obj = CollectionDataClass(values=[{'name': 'Alice', 'age': 35}, {'name': 'Bob', 'age': 40}])
    result = _asdict(collection_obj)
    assert isinstance(result, dict)
    assert len(result['values']) == 2
    assert result['values'][0]['name'] == 'Alice'
    assert result['values'][1]['name'] == 'Bob'