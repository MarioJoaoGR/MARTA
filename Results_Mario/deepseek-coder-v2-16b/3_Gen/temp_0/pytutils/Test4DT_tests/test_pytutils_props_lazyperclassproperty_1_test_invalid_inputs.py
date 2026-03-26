
import pytest
from pytutils.props import lazyperclassproperty

def test_invalid_inputs():
    # Test with an integer (non-function type)
    with pytest.raises(TypeError):
        @lazyperclassproperty(42)  # Passing an int instead of a function
        def cached_result(cls):
            pass
