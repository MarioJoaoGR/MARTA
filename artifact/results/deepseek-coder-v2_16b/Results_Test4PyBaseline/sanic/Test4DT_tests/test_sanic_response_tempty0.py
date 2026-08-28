# Module: sanic.response
import pytest
from sanic.response import HTTPResponse, empty

# Test default usage of the empty function
def test_empty_default():
    response = empty()
    assert response.status == 204
    assert not response.body
    assert isinstance(response, HTTPResponse)

# Test custom status code in the empty function
@pytest.mark.parametrize("status", [200, 201, 202, 203, 205, 206, 207, 208, 209, 299])
def test_empty_custom_status(status):
    response = empty(status=status)
    assert response.status == status
    assert not response.body
    assert isinstance(response, HTTPResponse)

# Test custom headers in the empty function
def test_empty_custom_headers():
    headers = {"X-Custom-Header": "Value"}
    response = empty(headers=headers)
    assert response.status == 204
    assert not response.body
    assert response.headers == headers
    assert isinstance(response, HTTPResponse)

# Test combination of custom status code and headers in the empty function
@pytest.mark.parametrize("status", [200, 201, 202, 203, 205, 206, 207, 208, 209, 299])
def test_empty_custom_status_and_headers(status):
    headers = {"X-Custom-Header": "Value"}
    response = empty(status=status, headers=headers)
    assert response.status == status
    assert not response.body
    assert response.headers == headers
    assert isinstance(response, HTTPResponse)
