# Module: sanic.response
import pytest
from .http_response import HTTPResponse  # Assuming the module is correctly imported and HTTPResponse is defined here
from typing import Dict, Optional

# Test cases for text function from sanic.response

def test_text_basic():
    response = text(body="Hello, World!")
    assert isinstance(response, HTTPResponse), "Expected an instance of HTTPResponse"
    assert response.body == b"Hello, World!", "Body content does not match the expected value"
    assert response.status == 200, "Default status code is incorrect"
    assert response.headers == {}, "Headers should be empty by default"
    assert response.content_type == "text/plain; charset=utf-8", "Content type does not match the expected value"

def test_text_custom_status():
    response = text(body="Hello, World!", status=201)
    assert isinstance(response, HTTPResponse), "Expected an instance of HTTPResponse"
    assert response.body == b"Hello, World!", "Body content does not match the expected value"
    assert response.status == 201, "Custom status code is incorrect"
    assert response.headers == {}, "Headers should be empty by default"
    assert response.content_type == "text/plain; charset=utf-8", "Content type does not match the expected value"

def test_text_custom_headers():
    headers = {"X-Custom-Header": "Value"}
    response = text(body="Hello, World!", status=200, headers=headers)
    assert isinstance(response, HTTPResponse), "Expected an instance of HTTPResponse"
    assert response.body == b"Hello, World!", "Body content does not match the expected value"
    assert response.status == 200, "Status code is incorrect"
    assert response.headers == headers, "Custom headers do not match the expected values"
    assert response.content_type == "text/plain; charset=utf-8", "Content type does not match the expected value"

def test_text_custom_content_type():
    response = text(body="Hello, World!", content_type="application/json")
    assert isinstance(response, HTTPResponse), "Expected an instance of HTTPResponse"
    assert response.body == b"Hello, World!", "Body content does not match the expected value"
    assert response.status == 200, "Status code is incorrect"
    assert response.headers == {}, "Headers should be empty by default"
    assert response.content_type == "application/json", "Content type does not match the expected value"

def test_text_invalid_body():
    with pytest.raises(TypeError):
        text(body=123)  # Invalid body type, should raise TypeError
