
from sanic import Sanic
from sanic.response import text as sanic_text
import pytest

# Create a new instance of Sanic for each test
@pytest.fixture(scope="module")
def app():
    return Sanic("TestApp")

# Test the creation of an HTTP response with valid input parameters

# Test the creation of an HTTP response with a non-string body
def test_invalid_body_type(app):
    # Define invalid input parameters
    body = 12345
    status = 200
    headers = {"Content-Type": "text/plain"}
    content_type = "text/plain; charset=utf-8"
    
    # Call the function under test and expect a TypeError
    with pytest.raises(TypeError):
        sanic_text(body, status=status, headers=headers, content_type=content_type)