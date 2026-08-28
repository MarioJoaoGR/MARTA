
# Module: sanic.router
import pytest
from sanic import Sanic
from sanic.router import Router  # Corrected import statement
from sanic.exceptions import SanicException, NotFound

# Fixture to create a new instance of the Router class for each test
@pytest.fixture
def router():
    return Router()

# Test case to check if an invalid route raises a SanicException with the correct message
def test_invalid_route(router):
    # Adding an invalid route that contains '__' in its labels
    def custom_handler(request):
        pass
    router.add("/invalid__route", ["GET"], custom_handler)
    
    # Attempt to finalize the router and expect a SanicException to be raised
    with pytest.raises(SanicException) as excinfo:
        router.finalize()
    
    # Check if the exception message contains the correct invalid route information
    assert "Invalid route" in str(excinfo.value)
    assert "__route" in str(excinfo.value)

# Test case to check if a valid route does not raise an exception
def test_valid_route(router):
    # Adding a valid route without '__' in its labels
    def custom_handler(request):
        pass
    router.add("/valid_route", ["GET"], custom_handler)
    
    # Finalize the router and expect no exception to be raised
    try:
        router.finalize()
    except SanicException:
        pytest.fail("Unexpected SanicException raised for a valid route")

# Test case to check if multiple routes are processed correctly without raising exceptions
def test_multiple_routes(router):
    # Adding two routes, one valid and one invalid
    def custom_handler1(request):
        pass
    router.add("/valid_route1", ["GET"], custom_handler1)
    
    def custom_handler2(request):
        pass
    router.add("/invalid__route2", ["GET"], custom_handler2)
    
    # Attempt to finalize the router and expect a SanicException for the invalid route
    with pytest.raises(SanicException) as excinfo:
        router.finalize()
    
    assert "Invalid route" in str(excinfo.value)
    assert "__route2" in str(excinfo.value)

# Integration test to ensure that the Sanic app can be run with a finalized router without raising exceptions
def test_sanic_app_integration():
    # Create a new Sanic application and add routes using the router
    app = Sanic("MyApp")
    router = Router()  # Corrected instantiation
    
    @app.route("/valid_route", methods=["GET"])
    async def valid_handler(request):
        return request.json({"message": "Valid route"})
    
    # Add the routes to the router and finalize it
    router.add("/valid_route", ["GET"], valid_handler)
    try:
        router.finalize()
    except SanicException:
        pytest.fail("Unexpected SanicException raised during finalization")
    
    # Run the Sanic app and ensure no exceptions are raised
    app.run(host="127.0.0.1", port=8000)
