# Module: sanic.mixins.exceptions
# test_sanic_mixins_exceptions.py
from sanic import Sanic
from sanic.blueprints import Blueprint
from sanic.exceptions import SanicException
from sanic.mixins import ExceptionMixin
import pytest

# Define a custom exception that inherits from Sanic's base exception
class FutureException(SanicException):
    pass

# Create a Sanic app and blueprint for demonstration
app = Sanic("MyApp")
bp = Blueprint("ExampleBlueprint", url_prefix="/example")

# Add the ExceptionMixin to the blueprint
class SomeClass(ExceptionMixin):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._future_exceptions: Set[FutureException] = set()

    # Override _apply_exception_handler to provide specific handling logic
    def _apply_exception_handler(self, handler: FutureException) -> None:
        print(f"Caught future exception: {handler}")

# Register the blueprint with the app and add the exception mixin
bp = SomeClass()
app.blueprint(bp)

# Define a route that raises a custom exception
@bp.route("/raise-exception")
async def raise_exception(request):
    raise FutureException("This is a future exception")

# Register an exception handler for the blueprint
@bp.exception(FutureException, apply=True)
def handle_future_exception(request, exception):
    return json({"error": str(exception)}, status=400)

# Test cases
def test_custom_exception():
    client = app.test_client
    response = client.get("/raise-exception")
    assert response.status == 400
    assert response.json["error"] == "This is a future exception"

def test_exception_handler():
    client = app.test_client
    response = client.get("/raise-exception")
    assert response.status == 400
    assert response.json["error"] == "This is a future exception"

if __name__ == "__main__":
    pytest.main()
