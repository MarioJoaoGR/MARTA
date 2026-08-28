
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError

@dataclass
class MyClass:
    known_param1: int
    known_param2: str

class _RaiseUndefinedParameters:
    @staticmethod
    def handle_from_dict(cls, kvs: Dict) -> Dict[str, Any]:
        known = {k: v for k, v in kvs.items() if hasattr(cls, k)}
        unknown = {k: v for k, v in kvs.items() if not hasattr(cls, k)}
        if len(unknown) > 0:
            raise UndefinedParameterError(
                f"Received undefined initialization arguments {unknown}")
        return known




def test_no_parameters():
    kvs_empty = {}
    result = _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs_empty)
    assert result == {}

def test_only_unknown_parameters():
    kvs_only_unknown = {'unknown_param1': 42, 'unknown_param2': 'example'}
    with pytest.raises(UndefinedParameterError) as excinfo:
        _RaiseUndefinedParameters.handle_from_dict(MyClass, kvs_only_unknown)
    assert str(excinfo.value) == "Received undefined initialization arguments {'unknown_param1': 42, 'unknown_param2': 'example'}"