
import pytest
from sanic import Sanic, Blueprint

# Define a simple logging middleware function
def log_request(req):
    print(f"Request method: {req.method}, URL: {req.url}")

# Create a fixture for the app and blueprints
@pytest.fixture
def create_app():
    app = Sanic("MyApp")
    bp1 = Blueprint("bp1", url_prefix="/bp1")
    
    # Define routes in the blueprint
    @bp1.route('/hello')
    async def hello_world(request):
        return "Hello, world!"
    
    app.blueprint(bp1)
    yield app

# Test for registering middleware for all blueprints

# Test for registering middleware with additional arguments

# Test for invalid input (name conflict)
def test_invalid_input():
    with pytest.raises(Exception):
        # Attempt to create a Sanic app with the same name twice
        Sanic("MyApp")
        Sanic("MyApp")