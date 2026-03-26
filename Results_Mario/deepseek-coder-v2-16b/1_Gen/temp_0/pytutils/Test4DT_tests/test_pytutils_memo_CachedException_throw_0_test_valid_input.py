
# Importing CachedException from pytutils.memo
from pytutils.memo import CachedException

def test_valid_input():
    # Define a custom exception for testing
    class CustomError(Exception):
        pass
    
    # Create an instance of the custom error with a message
    ex = CustomError("An error occurred")
    
    # Instantiate CachedException with the custom error
    cached_exception = CachedException(ex)
    
    # Test that calling throw raises the exception correctly
    try:
        cached_exception.throw()
    except CustomError as e:
        assert str(e) == "An error occurred"
