
# Import the Try class from the pymonet.monad_try module
from pymonet.monad_try import Try

def test_invalid_input():
    # Create an instance of Try with invalid input (None, False)
    try_instance = Try(None, False)
    
    # Define a mock fail callback function that prints the error message
    def print_error(value):
        assert value == None  # Ensure the value is None
    
    # Call on_fail with the mock fail callback function
    try_instance.on_fail(print_error)
