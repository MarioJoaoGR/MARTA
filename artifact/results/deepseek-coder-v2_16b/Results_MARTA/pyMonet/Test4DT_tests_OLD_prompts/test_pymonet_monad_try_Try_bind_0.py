
import pytest
from pymonet.monad_try import Try


def test_invalid_inputs():
    success = Try(42, True)
    failure = Try("error", False)
    
    def double(x):
        return Try(x * 2, True)
    
    # Invalid binder function (not callable) should raise TypeError
    with pytest.raises(TypeError):
        success.bind("not a function")
    
    # Invalid value type for bind method should also raise TypeError
    with pytest.raises(TypeError):
        success.bind(42)  # Passing an integer instead of a function