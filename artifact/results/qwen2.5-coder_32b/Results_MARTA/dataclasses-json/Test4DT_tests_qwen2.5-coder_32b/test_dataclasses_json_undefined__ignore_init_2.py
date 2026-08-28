
import pytest
from dataclasses import dataclass, fields
import inspect
import functools

# Importing necessary classes and functions from the module
from dataclasses_json.undefined import _CatchAllUndefinedParameters, _IgnoreUndefinedParameters

@dataclass
class MyClass:
    param1: str
    param2: int

# Modify the __init__ method to ignore undefined parameters
MyClass.__init__ = _IgnoreUndefinedParameters.create_init(MyClass)

def test_myclass_initialization_with_known_parameters():
    """Test initialization with known parameters."""
    obj = MyClass(param1='value1', param2=42)
    assert obj.param1 == 'value1'
    assert obj.param2 == 42

def test_myclass_initialization_with_extra_parameters():
    """Test initialization with extra parameters that should be ignored."""
    obj = MyClass(param1='value1', param2=42, extra_param='ignored')
    assert obj.param1 == 'value1'
    assert obj.param2 == 42

def test_myclass_initialization_with_missing_parameters():
    """Test initialization with missing parameters, which should raise a TypeError."""
    with pytest.raises(TypeError):
        MyClass(param1='value1')

def test_myclass_initialization_with_only_extra_parameters():
    """Test initialization with only extra parameters that should raise a TypeError."""
    with pytest.raises(TypeError):
        MyClass(extra_param='ignored')
