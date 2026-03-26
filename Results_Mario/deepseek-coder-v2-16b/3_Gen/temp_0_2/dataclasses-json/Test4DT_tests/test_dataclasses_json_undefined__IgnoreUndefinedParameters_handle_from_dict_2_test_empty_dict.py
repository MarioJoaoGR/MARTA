
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any
from dataclasses_json.undefined import _IgnoreUndefinedParameters, _UndefinedParameterAction

@dataclass
class ExampleClass:
    field1: int
    field2: str

def test_empty_dict():
    kvs = {}
    result = _IgnoreUndefinedParameters.handle_from_dict(ExampleClass, kvs)
    assert result == {}
