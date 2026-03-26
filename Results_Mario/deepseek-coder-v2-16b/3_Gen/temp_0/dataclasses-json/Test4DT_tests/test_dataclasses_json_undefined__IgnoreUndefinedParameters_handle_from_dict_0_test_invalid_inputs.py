
import pytest
from dataclasses import fields, is_dataclass
from typing import Dict, Any
from dataclasses_json.undefined import _IgnoreUndefinedParameters
from dataclasses_json.undefined import _UndefinedParameterAction

class DummyClass:
    pass

def test_handle_from_dict_invalid_inputs():
    cls = DummyClass
    kvs = {'param1': 1, 'extra_param': 2}
    
    with pytest.raises(TypeError):
        result = _IgnoreUndefinedParameters.handle_from_dict(cls=cls, kvs=kvs)
