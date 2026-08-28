
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any
from unittest.mock import patch
import dataclasses_json

# Define the _CatchAllUndefinedParameters class and handle_dump method as provided in the function code block
class _CatchAllUndefinedParameters:
    def handle_dump(obj) -> Dict[Any, Any]:
        catch_all_field = _CatchAllUndefinedParameters._get_catch_all_field(cls=obj)
        return getattr(obj, catch_all_field.name)
    
    @staticmethod
    def _get_catch_all_field(cls):
        for field in fields(cls):
            if isinstance(field.type, utils.CatchAll):
                return field
        raise AttributeError("No CatchAll field found in dataclass")

# Test valid case where handle_dump should work correctly

# Test edge case where handle_dump should raise AttributeError due to missing CatchAll field
def test_edge_case():
    @dataclass
    class Config:
        param1: int
        param2: str = "default"
        catch_all: dict = None
    
    config = Config(param1=10)
    with pytest.raises(AttributeError):
        dataclasses_json._CatchAllUndefinedParameters.handle_dump(config)