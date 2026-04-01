
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import _RaiseUndefinedParameters, UndefinedParameterError

@dataclass
class TestClass:
    param1: int
    param2: str

def test_invalid_input():
    with pytest.raises(UndefinedParameterError):
        kvs = {'param1': 1, 'extra_param': 2}
        _RaiseUndefinedParameters.handle_from_dict(TestClass, kvs)
