
import pytest
from dataclasses import dataclass, field, fields
from dataclasses_json import dataclass_json
import warnings

# Assuming the function is defined in a module named 'dataclasses_json.core'
from dataclasses_json.core import _decode_dataclass

@pytest.fixture
def example_dataclass():
    @dataclass_json
    @dataclass
    class ExampleDataclass:
        int_field: int = 0
        str_field: str = "default"
    
    return ExampleDataclass, {'int_field': 42, 'str_field': 'test'}

def test_decode_dataclass_basic(example_dataclass):
    cls, kvs = example_dataclass
    instance = _decode_dataclass(cls, kvs, infer_missing=False)
    assert isinstance(instance.int_field, int)
    assert instance.int_field == 42
    assert isinstance(instance.str_field, str)
    assert instance.str_field == 'test'

def test_decode_dataclass_infer_missing():
    @dataclass_json
    @dataclass
    class ExampleDataclass:
        int_field: int = 0
        str_field: str = "default"
    
    instance = _decode_dataclass(ExampleDataclass, {'int_field': 42}, infer_missing=True)
    assert isinstance(instance.int_field, int)
    assert instance.int_field == 42
    assert isinstance(instance.str_field, str)
    assert instance.str_field == "default"

def test_decode_dataclass_none_infer_missing():
    @dataclass_json
    @dataclass
    class ExampleDataclass:
        int_field: int = 0
        str_field: str = "default"
    
    instance = _decode_dataclass(ExampleDataclass, {'int_field': None}, infer_missing=True)