
import pytest
from flutes.exception import exception_wrapper

def handler_fn(e, one, two, *args, my_arg=None, **kwargs):
    assert isinstance(e, ValueError)
    assert one == 1
    assert two == "2"
    assert args == ("arg1", "arg2")
    assert my_arg is None
    assert kwargs == {"four": 4}

@pytest.mark.xfail(raises=ValueError)
def test_valid_case():
    @exception_wrapper(handler_fn)
    def foo(one, two, *args, three=None, **kwargs):
        raise ValueError("Test error")
    
    foo(1, "2", "arg1", "arg2", four=4)
