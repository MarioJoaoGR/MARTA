
import pytest
from flutes.multiproc import DummyApplyResult

def test_valid_input():
    value = 42  # Example value of type T
    dummy_result = DummyApplyResult(value)  # Create an instance with the given value
    
    assert dummy_result._value == value  # Check if the value is stored correctly
    dummy_result.wait()  # Call the wait method to ensure it does not raise errors or have side effects
