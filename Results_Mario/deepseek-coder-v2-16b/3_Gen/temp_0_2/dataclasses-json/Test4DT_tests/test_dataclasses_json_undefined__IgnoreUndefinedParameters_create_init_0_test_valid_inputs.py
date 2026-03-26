
import pytest
from dataclasses import dataclass
from dataclasses_json.undefined import _IgnoreUndefinedParameters

@dataclass
class MockClass:
    x: int = None
    y: int = None

def test_valid_inputs():
    mock_class = MockClass
    obj = mock_class()
    assert isinstance(obj, MockClass)
