
import pytest
from sanic import Sanic
from sanic.exceptions import abort, SanicException
from unittest.mock import patch

# Define a sample status codes dictionary for testing purposes
STATUS_CODES = {
    404: b"Not Found",
    500: b"Internal Server Error"
}

def test_abort_with_custom_message():
    with pytest.raises(SanicException) as excinfo:
        abort(404, "The requested resource was not found.")
    assert excinfo.value.status_code == 404
    assert str(excinfo.value) == "The requested resource was not found."

def test_abort_with_default_message():
    with pytest.raises(SanicException) as excinfo:
        abort(500)
    assert excinfo.value.status_code == 500
    assert str(excinfo.value) == "Internal Server Error"

def test_abort_without_message():
    with pytest.raises(SanicException) as excinfo:
        abort(404)
    assert excinfo.value.status_code == 404
    assert str(excinfo.value) == "Not Found"

# Mock the STATUS_CODES dictionary to simulate its behavior in tests
@patch('sanic.exceptions.STATUS_CODES', STATUS_CODES)
def test_abort_with_mocked_status_codes():
    with pytest.raises(SanicException) as excinfo:
        abort(404, "The requested resource was not found.")
    assert excinfo.value.status_code == 404
    assert str(excinfo.value) == "The requested resource was not found."
