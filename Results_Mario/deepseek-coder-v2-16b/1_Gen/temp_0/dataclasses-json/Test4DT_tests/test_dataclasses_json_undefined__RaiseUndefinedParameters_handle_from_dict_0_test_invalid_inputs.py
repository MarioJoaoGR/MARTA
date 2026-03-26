
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError

# Assuming _RaiseUndefinedParameters and handle_from_dict are defined in a module named dataclasses_json.undefined
from dataclasses_json.undefined import _RaiseUndefinedParameters  # Adjust the import path as necessary

@dataclass
class TestClass:
    param1: int
    param2: str

def test_handle_from_dict_valid():
    kvs = {'param1': 1, 'param2': 'value'}
    result = _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs)
    assert result == {'param1': 1, 'param2': 'value'}

def test_handle_from_dict_invalid():
    kvs = {'param1': 1, 'extra_param': 'value'}
    with pytest.raises(UndefinedParameterError):
        _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs)
