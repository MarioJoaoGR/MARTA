
import pytest
from pymonet.monad_try import Try

def test_error_handling():
    try_object = Try('unexpected', True)
    
    # Define a filterer function that raises an error
    def invalid_filterer(value):
        raise ValueError("Test Error")
    
    # Test the filter method with the invalid filterer function
    with pytest.raises(ValueError):
        try_object.filter(invalid_filterer)
