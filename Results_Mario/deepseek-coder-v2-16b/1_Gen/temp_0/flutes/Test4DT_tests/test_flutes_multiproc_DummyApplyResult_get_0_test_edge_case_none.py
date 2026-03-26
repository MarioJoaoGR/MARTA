
import pytest
from flutes.multiproc import DummyApplyResult  # Assuming this is the correct module path

# Test case for get method in DummyApplyResult class
def test_get_method():
    # Create an instance of DummyApplyResult with a sample value
    dummy_result = DummyApplyResult(42)
    
    # Test retrieving the stored value without a timeout
    assert dummy_result.get() == 42
    
    # Test retrieving the stored value with a specified timeout (e.g., 1 second)
    assert dummy_result.get(timeout=1.0) == 42
