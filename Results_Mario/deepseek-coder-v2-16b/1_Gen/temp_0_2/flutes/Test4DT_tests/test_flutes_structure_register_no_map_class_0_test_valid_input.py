
import pytest
from typing import List, Type
from flutes.structure import register_no_map_class, _NO_MAP_TYPES

# Define a mock class that subclasses List for testing purposes
class MyCustomContainer(List):
    pass

def test_valid_input():
    # Register the custom container type
    register_no_map_class(MyCustomContainer)
    
    # Check if the custom container type is in _NO_MAP_TYPES set
    assert MyCustomContainer in _NO_MAP_TYPES, "_NO_MAP_TYPES does not contain MyCustomContainer"
