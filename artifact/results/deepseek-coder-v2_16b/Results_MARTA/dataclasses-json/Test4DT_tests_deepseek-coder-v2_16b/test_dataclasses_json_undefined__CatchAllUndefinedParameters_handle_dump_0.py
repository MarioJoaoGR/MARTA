
import pytest
from dataclasses import dataclass, fields
from typing import Optional, Dict, Any
from dataclasses_json.undefined import UndefinedParameterError, _CatchAllUndefinedParameters

# Define a simple dataclass for testing
@dataclass
class Person:
    name: str
    age: int
    address: str = None

# Define an invalid input class for testing the error handling
@dataclass
class InvalidInput:
    field: Any


def test_invalid_input():
    invalid = InvalidInput(field='not an integer')
    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_dump(invalid)