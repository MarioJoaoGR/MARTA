
import pytest
from pymonet.monad_try import Try
from pymonet.lazy import Lazy

def test_edge_case():
    # Define a function that might raise an exception
    def risky_function(x):
        if x == 0:
            raise ValueError("Cannot divide by zero")
        return 1 / x

    # Create a Lazy instance with the risky function
    lazy = Lazy(risky_function)

    # Call to_try method which should call the risky function and handle exceptions
    try_monad = lazy.to_try(0)  # This will raise an exception, so it should be handled by Try

    # Check if the Try monad represents the error correctly
    assert not try_monad.is_success
    assert isinstance(try_monad.value, ValueError)
    assert str(try_monad.value) == "Cannot divide by zero"
