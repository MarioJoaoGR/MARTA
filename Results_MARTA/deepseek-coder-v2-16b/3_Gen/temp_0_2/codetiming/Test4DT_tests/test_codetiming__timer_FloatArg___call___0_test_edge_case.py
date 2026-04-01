
from codetiming._timer import FloatArg
import pytest

def test_floatarg_callable():
    # Create a mock or dummy implementation of FloatArg for testing purposes
    class MockFloatArg(FloatArg):
        def __call__(self, __seconds: float) -> 'MockFloatArg':
            return self

    # Instantiate the mock class
    mock_instance = MockFloatArg()
    
    # Call the __call__ method and check if it returns the instance itself
    assert mock_instance(3.5) == mock_instance
