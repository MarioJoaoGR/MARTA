
import pytest
from flutes.exception import exception_wrapper

# Mock handler function for testing purposes
def mock_handler(e, *args, **kwargs):
    pass

@pytest.mark.xfail(reason="Expected ValueError due to varargs argument in handler")
def test_edge_case():
    @exception_wrapper(mock_handler)
    def func_with_varargs(*args, **kwargs):
        pass
    
    with pytest.raises(ValueError):
        func_with_varargs()
