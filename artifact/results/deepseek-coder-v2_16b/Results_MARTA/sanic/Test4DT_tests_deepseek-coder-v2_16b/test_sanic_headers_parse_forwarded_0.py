
import pytest
from sanic import Sanic
from sanic.compat import Header
from typing import Dict, Union, Optional
from unittest.mock import patch

# Define the function to be tested
def parse_forwarded(headers, config) -> Optional[Dict[str, Union[int, str]]]:
    """Parse RFC 7239 Forwarded headers according to the specified configuration.

    This function processes the "Forwarded" HTTP header from a dictionary of request headers and a configuration object. It checks if the `by` or `secret` value matches the configured `FORWARDED_SECRET`. If they match, it parses the header content in reverse order for key-value pairs and returns them normalized according to specific rules.

    Parameters:
        headers (MultiDict): A dictionary-like object containing HTTP request headers, including the "Forwarded" header.
        config (Config): An object that contains configuration settings, specifically `FORWARDED_SECRET`.

    Returns:
        Optional[Dict[str, Union[int, str]]]: A dictionary with normalized key-value pairs from the parsed "Forwarded" header if a match is found; otherwise, returns None. The values are either integers or strings after normalization.
    """
    # Your implementation here
    pass

# Test scenarios
@pytest.mark.asyncio
async def test_parse_forwarded_with_matching_secret():
    app = Sanic("MyApp")
    
    @app.route("/forwarded")
    async def test_parse_forwarded(request):
        headers = Header({'forwarded': ['by=Example Corp', 'host=example.com']})
        config = Config(FORWARDED_SECRET='secret')
        result = parse_forwarded(headers, config)
        assert result == {'by': 'Example Corp', 'host': 'example.com'}
    
    with patch('sanic.app.Config', autospec=True):
        await app.test_client.get("/forwarded")

@pytest.mark.asyncio
async def test_parse_forwarded_without_matching_secret():
    app = Sanic("MyApp")
    
    @app.route("/forwarded")
    async def test_parse_forwarded(request):
        headers = Header({'forwarded': ['by=Example Corp', 'host=example.com']})
        config = Config(FORWARDED_SECRET='wrong-secret')
        result = parse_forwarded(headers, config)
        assert result is None
    
    with patch('sanic.app.Config', autospec=True):
        await app.test_client.get("/forwarded")

@pytest.mark.asyncio
async def test_parse_forwarded_without_header():
    app = Sanic("MyApp")
    
    @app.route("/forwarded")
    async def test_parse_forwarded(request):
        headers = Header({})
        config = Config(FORWARDED_SECRET='secret')
        result = parse_forwarded(headers, config)
        assert result is None
    
    with patch('sanic.app.Config', autospec=True):
        await app.test_client.get("/forwarded")
