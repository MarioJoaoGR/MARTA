
import pytest
from sanic.exceptions import SanicException

# Test Case 2: Raising an Exception with a Custom Message and Status Code
def test_sanic_exception_with_custom_message_and_status_code():
    try:
        raise SanicException("This is a test error", status_code=404)
    except SanicException as e:
        assert str(e) == "This is a test error"
        assert hasattr(e, 'status_code'), f"Expected status_code to be set but it was not."