
import pytest
from sanic import Sanic, response
from sanic.exceptions import MethodNotSupported

# Test Case 1: Raising an Exception with Custom Message and Allowed Methods
def test_method_not_supported_exception():
    try:
        raise MethodNotSupported("POST operation is not allowed", "POST", ["GET", "HEAD"])
    except MethodNotSupported as e:
        assert str(e) == "POST operation is not allowed"
        assert e.headers["Allow"] == "GET, HEAD"

# Test Case 2: Raising an Exception with Different Method and Allowed Methods
def test_method_not_supported_exception_different_method():
    try:
        raise MethodNotSupported("DELETE operation is not allowed", "DELETE", ["GET", "POST"])
    except MethodNotSupported as e:
        assert str(e) == "DELETE operation is not allowed"