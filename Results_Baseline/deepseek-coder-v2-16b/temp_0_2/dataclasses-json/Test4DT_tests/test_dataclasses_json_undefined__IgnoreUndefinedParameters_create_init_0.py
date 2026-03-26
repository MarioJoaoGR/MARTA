
import pytest
from dataclasses import dataclass
import inspect
import functools

# Import the function to be tested
from dataclasses_json.undefined import _IgnoreUndefinedParameters

@dataclass
class MyClass:
    param1: int
    param2: str

def test_create_init_with_defined_parameters():
    # Create the new initialization method for MyClass
    new_init = _IgnoreUndefinedParameters.create_init(MyClass)
    
    # Override the original __init__ method with the new one
    MyClass.__init__ = new_init

    # Example usage of MyClass with defined parameters
    my_instance = MyClass(param1=1, param2="value")
    assert isinstance(my_instance, MyClass)
    assert my_instance.param1 == 1