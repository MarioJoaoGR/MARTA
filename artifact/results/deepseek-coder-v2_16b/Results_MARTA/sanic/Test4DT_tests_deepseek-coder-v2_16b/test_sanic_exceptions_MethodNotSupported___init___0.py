
import pytest
from sanic import Sanic
from sanic.response import text
from sanic.exceptions import MethodNotSupported

# Test scenario 1: Raising MethodNotSupported exception with valid parameters
def test_method_not_supported():
    message = "This operation is not supported"
    method = "POST"
    allowed_methods = ["GET", "HEAD"]
    
    with pytest.raises(MethodNotSupported) as exc_info:
        raise MethodNotSupported(message, method, allowed_methods)
    
    assert str(exc_info.value) == message
    assert exc_info.value.headers["Allow"] == ", ".join(allowed_methods)

# Test scenario 2: Handling MethodNotSupported exception in a Sanic application