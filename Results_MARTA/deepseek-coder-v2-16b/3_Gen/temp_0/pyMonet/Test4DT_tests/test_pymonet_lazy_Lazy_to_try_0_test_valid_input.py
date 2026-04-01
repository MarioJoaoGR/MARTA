
import pytest
from pymonet.lazy import Lazy
from pymonet.monad_try import Try

def test_valid_input():
    # Define a function that will be stored in the Lazy instance
    def square(x):
        return x * x
    
    # Create a Lazy instance with the square function
    lazy = Lazy(square)
    
    # Call to_try method with a valid input (e.g., 5)
    try_monad = lazy.to_try(5)
    
    # Check if the Try monad is successful and the value is correct
    assert try_monad.is_success
    assert try_monad.value == 25
