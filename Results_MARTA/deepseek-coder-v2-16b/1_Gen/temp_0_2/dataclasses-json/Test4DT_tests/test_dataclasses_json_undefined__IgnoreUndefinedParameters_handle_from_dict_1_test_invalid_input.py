
import pytest
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses_json.undefined import _IgnoreUndefinedParameters

@pytest.fixture
def mock_class():
    @dataclass
    class MockClass:
        param1: int
        param2: str
    
    return MockClass

def test_invalid_input(mock_class):
    kvs = {'param1': 1, 'extra_param': 'extra'}
    result = _IgnoreUndefinedParameters.handle_from_dict(mock_class, kvs)
    assert isinstance(result, dict)
    assert len(result) == 1
    assert 'param1' in result
