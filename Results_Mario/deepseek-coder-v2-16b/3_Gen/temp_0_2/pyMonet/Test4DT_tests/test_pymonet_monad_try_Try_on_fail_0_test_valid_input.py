
import pytest
from pymonet.monad_try import Try  # Adjust the import path as necessary based on actual module location

# Define a mock fail callback function for testing
def mock_fail_callback(value):
    print(f"Mocked Fail Callback: {value}")

# Test case for valid input scenario
def test_valid_input():
    try_instance = Try("Some result", True)  # Creating an instance of Try with a successful state
    
    # Since the operation is successful, `on_fail` should not call the callback
    assert try_instance.is_success == True
    
    # If you want to test that on_fail does nothing when is_success is True:
    try_instance.on_fail(mock_fail_callback)  # Calling on_fail with a mock function
    assert try_instance.is_success == True  # Ensure the success state remains unchanged
    
    # Now, let's create an instance that represents failure and test if it calls the callback
    fail_try_instance = Try("Some error", False)
    fail_try_instance.on_fail(mock_fail_callback)  # This should call the mock callback with "Some error"
    
    # You can add assertions in the mock function to verify its behavior, but for now, let's just ensure it ran without errors
