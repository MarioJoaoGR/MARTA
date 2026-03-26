
# Module: pymonet.either
import pytest
from pymonet.either import Left, Right  # Importing Right from pymonet.either

# Test cases for the `ap` method in the `Left` class
def test_left_ap():
    # Create a Left instance with an error message
    left_value = Left("error message")
    
    # Apply a monadic function to the contained value in a `Left` monad
    result = left_value.ap(None)  # Passing None as a placeholder for a monadic structure
    
    # Assert that the result is still a Left instance with the same error message
    assert isinstance(result, Left)
    assert result.value == "error message"

# Additional test cases to cover different scenarios and edge cases
def test_left_ap_with_function():
    # Create a Left instance with a function as the value
    left_value = Left(lambda x: x * 2)
    
    # Attempt to apply the function to another monadic structure (Right in this case)
    right_value = Right(42)
    result = left_value.ap(right_value)
    
    # Assert that the result is still a Left instance with the same function
    assert isinstance(result, Left)
    assert callable(result.value)  # Ensure the value is indeed a function

def test_left_ap_with_non_function():
    # Create a Left instance with a non-function value
    left_value = Left("not a function")
    
    # Attempt to apply this non-function value to another monadic structure
    right_value = Right(42)
    result = left_value.ap(right_value)
    
    # Assert that the result is still a Left instance with the original non-function value
    assert isinstance(result, Left)
    assert result.value == "not a function"

# Run the tests when this script is executed
if __name__ == "__main__":
    pytest.main()
