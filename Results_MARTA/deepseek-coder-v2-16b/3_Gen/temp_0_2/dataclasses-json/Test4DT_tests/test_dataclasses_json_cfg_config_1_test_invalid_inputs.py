
import pytest
from dataclasses_json.cfg import config, UndefinedParameterError
from dataclasses_json import Undefined, LetterCase
from typing import Optional, Callable, Dict, Union, TypeVar, List
import functools

T = TypeVar('T')
MarshmallowField = object  # Assuming this is a placeholder for the actual type

def test_invalid_inputs():
    # Test invalid undefined parameter action
    metadata = {}
    with pytest.raises(UndefinedParameterError) as excinfo:
        config(metadata, undefined="invalid_action")
    
    assert str(excinfo.value) == "Invalid undefined parameter action, must be one of ['INCLUDE', 'RAISE', 'EXCLUDE']"
