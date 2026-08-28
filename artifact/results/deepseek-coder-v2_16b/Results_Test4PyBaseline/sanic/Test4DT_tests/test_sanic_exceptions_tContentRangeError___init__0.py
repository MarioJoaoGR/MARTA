# Module: sanic.exceptions
import pytest
from sanic import Sanic, response
from sanic.exceptions import ContentRangeError

# Test initialization of ContentRangeError with a valid content range
def test_init_with_valid_content_range():
    message = "The requested range cannot be fulfilled."
    content_range = {'total': 100}
    error = ContentRangeError(message, content_range)
    
    assert str(error) == message
    assert error.headers == {"Content-Range": "bytes */100"}

# Test raising ContentRangeError in a Sanic route
def test_content_range_error_in_sanic():
    app = Sanic("MyApp")
    
    @app.route('/resource')
    async def handler(request):
        content_range = {'total': 100}
        try:
            raise ContentRangeError("The requested range cannot be fulfilled.", content_range)
        except ContentRangeError as e:
            return response.json({"error": str(e)}, status=416)
    
    request, _ = app.test_client.get('/resource')
    assert request.status == 416
    assert request.json == {"error": "The requested range cannot be fulfilled."}
