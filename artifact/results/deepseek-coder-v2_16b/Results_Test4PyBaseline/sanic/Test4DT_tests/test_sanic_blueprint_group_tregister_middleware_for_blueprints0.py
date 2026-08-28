# Module: sanic.blueprint_group
import pytest
from sanic import Sanic

# Import the function to be tested
# from your_module_name import register_middleware_for_blueprints

@pytest.fixture
def app():
    app = Sanic("MyApp")
    return app

def test_register_middleware_for_blueprints(app):
    # Define a simple middleware function that logs requests
    def log_request(request):
        print(f"Received request: {request.method} {request.url}")
    
    # Register the middleware function for all blueprints in the application
    app.register_middleware_for_blueprints(log_request)
    
    # Define a route to trigger the middleware
    @app.route('/')
    async def test(request):
        return request.json("Hello, world!")
    
    # Run the Sanic app in a separate thread (or use an event loop if you prefer)
    import threading
    thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 8000})
    thread.start()
    
    # You can add more assertions or checks here to verify the behavior of the middleware
    # For example, you might want to check if the log_request function was called correctly
    pass
