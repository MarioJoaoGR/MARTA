
import pytest
from flutes.exception import exception_wrapper

def test_invalid_inputs():
    @pytest.mark.xfail(raises=ValueError)
    def func_with_error(*args, **kwargs):
        raise ValueError("Test exception")
    
    with pytest.raises(ValueError):
        func_with_error()
