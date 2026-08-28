
import pytest
from sanic import response
from typing import Any, Optional, Dict, Callable
try:
    from .http_response import HTTPResponse  # Assuming this is the correct import for HTTPResponse
except ImportError:
    pass

# Test basic usage of json function
def test_json_basic():
    body = {"key": "value"}
    resp = response.json(body=body)
    assert resp.status == 200
    assert resp.content_type == "application/json"