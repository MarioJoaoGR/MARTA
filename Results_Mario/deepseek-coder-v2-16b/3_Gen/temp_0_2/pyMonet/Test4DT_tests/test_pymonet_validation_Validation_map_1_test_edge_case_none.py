
from pymonet.validation import Validation
import pytest

def test_edge_case_none():
    # Create a Validation instance with None as value and an empty list for errors
    val = Validation(None, [])
    
    # Define a mapper function that returns the input value if it's not None, otherwise returns 0
    def mapper(value):
        return value if value is not None else 0
    
    # Apply the map method with the defined mapper function
    mapped_val = val.map(mapper)
    
    # Check that the new Validation instance has a mapped value and no errors
    assert mapped_val.value == 0
    assert len(mapped_val.errors) == 0
