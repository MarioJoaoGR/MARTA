
import pytest
from flutes.exception import exception_wrapper

# Mock handler function for testing purposes
def mock_handler_fn(e, one, two=None):
    pass

@pytest.mark.xfail(reason="ValueError expected due to argument default value")
def test_valid_inputs():
    @exception_wrapper(mock_handler_fn)
    def foo(one, two, *args, three=None, **kwargs):
        pass

    with pytest.raises(ValueError):
        foo(1, "2", "arg1", "arg2", four=4)
