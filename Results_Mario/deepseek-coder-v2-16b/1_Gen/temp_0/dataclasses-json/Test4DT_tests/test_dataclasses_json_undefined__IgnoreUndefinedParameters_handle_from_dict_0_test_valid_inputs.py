
from dataclasses_json.undefined import _IgnoreUndefinedParameters, _UndefinedParameterAction
from typing import Dict, Any
import pytest

@pytest.fixture
def class_object():
    # Define a sample class for testing
    from dataclasses import dataclass

    @dataclass
    class SampleClass:
        param1: int
        param2: str

    return SampleClass

def test_valid_inputs(class_object):
    kvs = {'param1': 1, 'extra_param': 'unknown'}
    result = _IgnoreUndefinedParameters.handle_from_dict(cls=class_object, kvs=kvs)
    
    assert isinstance(result, dict)
    assert 'param1' in result
    assert len(result) == 1
