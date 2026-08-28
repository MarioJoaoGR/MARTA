
# Module: sanic.exceptions
import pytest
from sanic.exceptions import SanicException

# Test Case 1: Raising an Exception with a Custom Message
def test_sanic_exception_with_custom_message():
    try:
        raise SanicException("This is a test error")
    except SanicException as e:
        assert str(e) == "This is a test error"
        assert hasattr(e, 'status_code'), f"Expected status_code to be set but it was not."