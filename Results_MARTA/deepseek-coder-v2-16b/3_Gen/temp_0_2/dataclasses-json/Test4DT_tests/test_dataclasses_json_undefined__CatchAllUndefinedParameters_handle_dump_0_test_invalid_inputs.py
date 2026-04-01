
import pytest
from dataclasses_json.undefined import _CatchAllUndefinedParameters
from typing import Any, Dict

class InvalidClass:
    my_field: int = 0

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test case where the class does not have a catch-all field defined
        _CatchAllUndefinedParameters.handle_dump(InvalidClass)

    # Adding a second catch-all field to trigger the multiple catch-all error
    class InvalidClassWithMultipleCatchAlls:
        my_field1: int = 0
        my_field2: int = 0
        _catch_all: Any = None

    with pytest.raises(TypeError):
        # Test case where the class has multiple catch-all fields defined
        _CatchAllUndefinedParameters.handle_dump(InvalidClassWithMultipleCatchAlls)
