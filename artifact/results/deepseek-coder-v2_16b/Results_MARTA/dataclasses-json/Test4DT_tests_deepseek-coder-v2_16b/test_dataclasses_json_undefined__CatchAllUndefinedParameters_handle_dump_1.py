
import pytest
from dataclasses import dataclass, fields
from typing import Optional, Dict, Any
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError

# Define a simple dataclass for demonstration
@dataclass
class Person:
    name: str
    age: int
    address: str = None


def test_handle_dump_with_undefined_parameters():
    @dataclass
    class Config:
        param1: int
        param2: str = "default"
        catch_all: dict = None

    config = Config(param1=10)
    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_dump(config)