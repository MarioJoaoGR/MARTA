
import pytest
from isort.literal import register_type, type_mapping, ISortPrettyPrinter

def test_valid_input():
    @register_type('example_type', int)
    def example_function(value, printer):
        return str(value)
    
    assert 'example_type' in type_mapping
    assert type_mapping['example_type'][0] == int
    assert callable(type_mapping['example_type'][1])
