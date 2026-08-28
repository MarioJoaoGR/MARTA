# Module: sanic.router
# test_sanic_router.py
import pytest
from sanic import Sanic
from sanic.routerclass import Router
from sanic.exceptions import NotFound

@pytest.fixture
def router():
    return Router()

def test_default_method(router):
    assert router.DEFAULT_METHOD == 'GET'

def test_allowed_methods(router):
    assert isinstance(router.ALLOWED_METHODS, list)
    assert len(router.ALLOWED_METHODS) > 0

def test_routes_all_empty(router):
    assert router.routes_all() == []

def test_add_route(router):
    def handle_request(request):
        return request.json({"message": "Hello, World!"})
    
    router.add_route('/example', handle_request, ['GET'])
    assert len(router.routes_all()) == 1

def test_retrieve_all_routes(router):
    def handle_request(request):
        return request.json({"message": "Hello, World!"})
    
    router.add_route('/example', handle_request, ['GET'])
    all_routes = router.routes_all()
    assert len(all_routes) == 1
    assert '/example' in [route['path'] for route in all_routes]

def test_get_handler_found(router):
    def handle_request(request):
        return request.json({"message": "Hello, World!"})
    
    router.add_route('/hello', handle_request, ['GET'])
    try:
        route_info = router.get(path='/hello', method='GET', host=None)
        assert route_info is not None
    except NotFound as e:
        pytest.fail("Route should be found but raised NotFound exception: " + str(e))

def test_get_handler_not_found(router):
    try:
        router.get(path='/non_existent', method='GET', host=None)
        pytest.fail("Expected NotFound exception for non-existent route")
    except NotFound as e:
        assert str(e) == "Route not found"

def test_integration_with_sanic_app():
    app = Sanic("MyApp")
    router = Router()

    @app.route("/hello", methods=['GET'])
    async def hello_handler(request):
        return request.json({"message": "Hello, World!"})

    def custom_handler(request):
        return request.json({"message": "Custom route"})
    
    router.add_route("/custom", ['GET'], custom_handler)

    @app.route("/example", methods=['POST'])
    async def example_handler(request):
        return request.json({"message": "Example POST"})

    client = app.test_client

    # Test GET /hello route
    response = client.get('/hello')
    assert response.status == 200
    assert response.json['message'] == 'Hello, World!'

    # Test GET /custom route
    response = client.get('/custom')
    assert response.status == 200
    assert response.json['message'] == 'Custom route'

    # Test POST /example route
    response = client.post('/example')
    assert response.status == 200
    assert response.json['message'] == 'Example POST'

    # Test non-existent route
    with pytest.raises(NotFound):
        client.get('/non_existent')
