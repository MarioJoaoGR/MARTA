
import pytest
from sanic import Sanic, response
from sanic.exceptions import MethodNotSupported
from unittest.mock import patch

# Test Scenario 1: test_valid_inputs
def test_valid_inputs():
    with pytest.raises(MethodNotSupported) as exc_info:
        raise MethodNotSupported("This operation is not supported", "POST", ["GET", "HEAD"])
    
    assert str(exc_info.value) == "This operation is not supported"
    assert exc_info.value.headers["Allow"] == "GET, HEAD"

# Test Scenario 2: test_edge_cases
def test_edge_cases():
    with pytest.raises(MethodNotSupported) as exc_info:
        raise MethodNotSupported("Test edge case", None, [])
    
    assert str(exc_info.value) == "Test edge case"
    assert exc_info.value.headers["Allow"] == ""

# Test Scenario 3: test_invalid_inputs
def test_invalid_inputs():
    with pytest.raises(MethodNotSupported) as exc_info:
        raise MethodNotSupported("Invalid input", "PATCH", ["GET", "HEAD"])
    
    assert str(exc_info.value) == "Invalid input"
    assert exc_info.value.headers["Allow"] == "GET, HEAD"
