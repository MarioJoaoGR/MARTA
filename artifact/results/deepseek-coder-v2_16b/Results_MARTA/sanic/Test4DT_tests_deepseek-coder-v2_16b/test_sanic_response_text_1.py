
from sanic import Sanic
from sanic.response import text as sanic_text
import pytest

app = Sanic("TestApp")

@app.route("/test")
async def test(request):
    response = sanic_text(body="Hello, World!", status=200, headers={'Content-Type': 'text/plain'}, content_type='text/html')
    return response

def test_valid_inputs():
    response = sanic_text(body="Hello, World!", status=200, headers={'Content-Type': 'text/plain'}, content_type='text/html')
    assert response.status == 200
    assert response.headers['Content-Type'] == 'text/plain'
    assert response.body == b"Hello, World!"

def test_edge_cases():
    with pytest.raises(TypeError):
        sanic_text(body=None, status=0, headers={}, content_type='')

def test_invalid_inputs():
    with pytest.raises(TypeError):
        sanic_text(body=[], status=200, headers={'Content-Type': 'text/plain'}, content_type='text/html')
