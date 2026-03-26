
import pytest
from dataclasses import fields, dataclass
from typing import Dict, Tuple, List, Any
from dataclasses_json.undefined import _UndefinedParameterAction

@dataclass
class ExampleClass:
    field1: int
    field2: str

def test_empty_dict():
    kvs = {}
    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(ExampleClass, kvs)
    
    assert isinstance(known, dict), "Known parameters should be a dictionary"
    assert isinstance(unknown, dict), "Unknown parameters should be a dictionary"
    assert len(known) == 0, "Known parameters should be empty for an empty dictionary"
    assert len(unknown) == 0, "Unknown parameters should be empty for an empty dictionary"
