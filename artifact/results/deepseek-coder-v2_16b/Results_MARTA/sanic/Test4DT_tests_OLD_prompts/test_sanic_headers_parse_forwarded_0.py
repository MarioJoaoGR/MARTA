
import pytest
from unittest.mock import patch, MagicMock
from sanic import Sanic
from sanic.compat import Header
from typing import Dict, Union, Optional
from sanic.headers import parse_forwarded as original_parse_forwarded

# Define a mock Config class to mimic the behavior of the real Config class in Sanic
class Config:
    def __init__(self, FORWARDED_SECRET=None):
        self.FORWARDED_SECRET = FORWARDED_SECRET

# Mock the parse_forwarded function to return a predefined result for testing
def mock_parse_forwarded(headers, config):
    if "by=Example Corp" in headers.getall("forwarded") and config.FORWARDED_SECRET == "secret":
        return {"by": "Example Corp", "host": "example.com"}
    else:
        return None

# Define a fixture to create a Sanic app for testing
@pytest.fixture
def app():
    app = Sanic("MyApp")
    return app

# Test scenario 1: Basic usage with matching secret
def test_parse_forwarded_basic(app):
    with patch('sanic.headers.parse_forwarded', side_effect=mock_parse_forwarded):
        @app.route("/forwarded")
        async def test_parse_forwarded(request):
            headers = Header({'forwarded': ['by=Example Corp', 'host=example.com']})
            config = Config(FORWARDED_SECRET='secret')
            result = parse_forwarded(headers, config)
            assert result == {'by': 'Example Corp', 'host': 'example.com'}

# Test scenario 2: Usage with no matching secret

# Test scenario 3: Usage with no header provided