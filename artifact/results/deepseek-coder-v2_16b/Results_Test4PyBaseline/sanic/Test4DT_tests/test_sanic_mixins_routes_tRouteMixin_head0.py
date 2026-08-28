# Module: sanic.mixins.routes
# test_sanic.py
from sanic import Sanic
from sanic.response import text
import pytest

@pytest.fixture(scope="module")
def app():
    app = Sanic("MyApp")
    
    class MyRouteMixin(RouteMixin):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

    @app.route('/', methods=["GET"])
    def handle_request(request):
        return text("Hello, World!")

    @app.route('/post', methods=["POST"], strict_slashes=True)
    def handle_post_request(request):
        return text("This is a POST request")

    @app.websocket('/ws')
    async def handle_websocket(request, ws):
        while True:
            msg = await ws.recv()
            await ws.send(f"Echo: {msg}")

    app.static('/static', './static')

    @app.route('/api/v1', methods=["GET"], version=1)
    def handle_api_request(request):
        return text("This is API v1")

    my_instance = MyRouteMixin()
    app.register_listener(my_instance, 'before_server_start')
    
    return app

def test_get_route(app):
    request, response = app.test_client.get('/')
    assert response.status == 200
    assert response.text == "Hello, World!"

def test_post_route(app):
    request, response = app.test_client.post('/post')
    assert response.status == 200
    assert response.text == "This is a POST request"

def test_websocket_route(app):
    with app.test_client.websocket('/ws') as ws:
        ws.send("Hello")
        msg = ws.receive()
        assert msg == "Echo: Hello"

def test_static_file_route(app):
    request, response = app.test_client.get('/static/example.txt')  # Assuming example.txt exists in the static directory
    assert response.status == 200
    assert response.text == "File content"  # Replace with actual file content if known

def test_api_route(app):
    request, response = app.test_client.get('/api/v1')
    assert response.status == 200
    assert response.text == "This is API v1"
