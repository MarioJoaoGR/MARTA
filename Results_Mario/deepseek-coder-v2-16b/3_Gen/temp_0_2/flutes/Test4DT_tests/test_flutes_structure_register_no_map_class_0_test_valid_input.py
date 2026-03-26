
import pytest
from typing import Type
from flutes.structure import register_no_map_class, _NO_MAP_TYPES

# Define a mock class that subclasses a built-in container type for testing purposes
class MyCustomContainer(list):
    pass

def test_valid_input():
    # Register the custom container type
    register_no_map_class(MyCustomContainer)
    
    # Check if the custom container type is in _NO_MAP_TYPES
    assert MyCustomContainer in _NO_MAP_TYPES
