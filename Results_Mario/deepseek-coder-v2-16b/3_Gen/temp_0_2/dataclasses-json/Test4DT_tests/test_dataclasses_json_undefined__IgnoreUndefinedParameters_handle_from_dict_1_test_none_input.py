
import pytest
from dataclasses_json.undefined import _IgnoreUndefinedParameters
from typing import Dict, Any

class ExampleClass:
    field1: int
    field2: str

def test_none_input():
    with pytest.raises(TypeError):
        kvs = None
        result = _IgnoreUndefinedParameters.handle_from_dict(ExampleClass, kvs)
