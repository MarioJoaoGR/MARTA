
# Importing necessary modules from flutes.multiproc
from flutes.multiproc import DummyApplyResult

def test_edge_cases():
    # Test edge cases for DummyApplyResult class
    
    # Create a DummyApplyResult instance with an integer value
    result = DummyApplyResult(42)
    
    # Check if the application was successful
    assert result.success() is True, "Expected success to be True"
    
    # Create a DummyApplyResult instance with a string value
    result_str = DummyApplyResult("Success")
    
    # Check if the application was successful
    assert result_str.success() is True, "Expected success to be True for string value"
