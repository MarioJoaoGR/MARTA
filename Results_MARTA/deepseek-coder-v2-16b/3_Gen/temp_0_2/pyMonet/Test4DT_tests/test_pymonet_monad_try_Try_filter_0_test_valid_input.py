
import pytest
from pymonet.monad_try import Try

def test_valid_input():
    try_object = Try('success', True)
    
    # Define a filterer function that always returns True
    def valid_filterer(value):
        return True
    
    # Apply the filter method with the valid filterer function
    filtered_try_object = try_object.filter(valid_filterer)
    
    # Assert that the result is a Try object with the same value and is_success set to True
    assert isinstance(filtered_try_object, Try)
    assert filtered_try_object.value == 'success'
    assert filtered_try_object.is_success is True
