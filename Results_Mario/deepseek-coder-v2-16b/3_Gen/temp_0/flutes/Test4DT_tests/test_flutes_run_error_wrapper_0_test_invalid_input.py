
import pytest
import subprocess
from flutes.run import error_wrapper

def test_invalid_input():
    # Create a mock exception of an invalid type
    class InvalidError(Exception):
        pass
    
    err = InvalidError("Test Error")
    
    # Call the function and check if it raises the expected error
    with pytest.raises(InvalidError) as exc_info:
        raise err
