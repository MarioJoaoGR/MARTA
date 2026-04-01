
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any
from dataclasses_json.undefined import _IgnoreUndefinedParameters, _UndefinedParameterAction

@dataclass
class ExampleClass:
    field1: int
    field2: str

def test_valid_input():
    kvs = {'field1': 1, 'extra_param': 'value', 'field2': 'hello'}
    known_parameters = _IgnoreUndefinedParameters.handle_from_dict(ExampleClass, kvs)
    assert known_parameters == {'field1': 1, 'field2': 'hello'}
