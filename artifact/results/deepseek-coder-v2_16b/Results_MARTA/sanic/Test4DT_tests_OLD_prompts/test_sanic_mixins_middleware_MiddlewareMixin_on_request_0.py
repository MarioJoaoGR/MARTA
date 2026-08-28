
import pytest
from unittest.mock import patch, MagicMock
from sanic.mixins.middleware import MiddlewareMixin
from functools import partial

# Scenario 1: Basic Usage with Custom Middleware
@pytest.mark.asyncio
@patch('your_module.MyMiddleware')
async def test_basic_usage(mock_middleware):
    from sanic import Sanic
    from sanic.response import text
    
    app = Sanic("MyApp")
    mock_instance = MagicMock()
    mock_middleware.return_value = mock_instance
    
    # Register middleware to be applied globally (request level)
    @mock_instance.middleware
    def my_middleware_function(request):
        print("Processing request:", request)
    
    app.register_middleware(mock_instance, attach_to="request")
    
    @app.route('/')
    async def test(request):
        return text('Hello, world!')
    
    # Run the application
    loop = app.loop  # Assuming app.loop is correctly mocked or defined
    await loop()

# Scenario 2: Using Middleware Decorator
@pytest.mark.asyncio
@patch('your_module.MyMiddleware')
async def test_middleware_decorator(mock_middleware):
    from sanic import Sanic
    from sanic.response import text
    
    app = Sanic("MyApp")
    mock_instance = MagicMock()
    mock_middleware.return_value = mock_instance
    
    # Register middleware using a decorator (as if @app.middleware('request'))
    @mock_instance.middleware
    def my_middleware_function(request):
        print("Processing request:", request)
    
    app.register_middleware(mock_instance, attach_to="request")
    
    @app.route('/')
    async def test(request):
        return text('Hello, world!')
    
    # Run the application
    loop = app.loop  # Assuming app.loop is correctly mocked or defined
    await loop()

# Scenario 3: Middleware for Specific Route
@pytest.mark.asyncio
@patch('your_module.MyMiddleware')
async def test_middleware_specific_route(mock_middleware):
    from sanic import Sanic
    from sanic.response import text
    
    app = Sanic("MyApp")
    mock_instance = MagicMock()
    mock_middleware.return_value = mock_instance
    
    # Register middleware to be applied only to a specific route (e.g., '/specific')
    @app.route('/specific')
    async def specific(request):
        return text('This is a specific route!')
    
    mock_instance.on_request = MagicMock()
    mock_instance.on_request()(my_middleware_function)
    
    # Run the application
    loop = app.loop  # Assuming app.loop is correctly mocked or defined
    await loop()

# Scenario 4: Middleware for Response Processing
@pytest.mark.asyncio
@patch('your_module.MyMiddleware')
async def test_middleware_response_processing(mock_middleware):
    from sanic import Sanic
    from sanic.response import text
    
    app = Sanic("MyApp")
    mock_instance = MagicMock()
    mock_middleware.return_value = mock_instance
    
    # Register middleware to be applied during response processing
    @mock_instance.middleware
    def my_middleware_function(request, response):
        print("Processing response:", request, response)
    
    app.register_middleware(mock_instance, attach_to="response")
    
    @app.route('/')
    async def test(request):
        return text('Hello, world!')
    
    # Run the application
    loop = app.loop  # Assuming app.loop is correctly mocked or defined
    await loop()

# Scenario 5: Middleware for Specific Route with Parameters
@pytest.mark.asyncio
@patch('your_module.MyMiddleware')
async def test_middleware_specific_route_with_parameters(mock_middleware):
    from sanic import Sanic
    from sanic.response import text
    
    app = Sanic("MyApp")
    mock_instance = MagicMock()
    mock_middleware.return_value = mock_instance
    
    # Register middleware to be applied only to a specific route (e.g., '/specific')
    @app.route('/specific')
    async def specific(request):
        return text('This is a specific route!')
    
    mock_instance.on_request = MagicMock()
    mock_instance.on_request()(my_middleware_function)
    
    # Run the application
    loop = app.loop  # Assuming app.loop is correctly mocked or defined
    await loop()
