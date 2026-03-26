
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError

# Assuming _RaiseUndefinedParameters is defined in the module 'dataclasses_json.undefined'
from dataclasses_json.undefined import _RaiseUndefinedParameters as RaiseUndefinedParameters

@dataclass
class TestClass:
    param1: int
    param2: str

def test_invalid_inputs():
    with pytest.raises(UndefinedParameterError):
        # This should raise an UndefinedParameterError because 'param3' is not defined in the class
        RaiseUndefinedParameters.handle_from_dict(TestClass, {'param1': 1, 'param3': 'test'})

    # This should pass without raising an error since all provided keys are valid for the class fields
    result = RaiseUndefinedParameters.handle_from_dict(TestClass, {'param1': 1, 'param2': 'test'})
    assert result == {'param1': 1, 'param2': 'test'}
