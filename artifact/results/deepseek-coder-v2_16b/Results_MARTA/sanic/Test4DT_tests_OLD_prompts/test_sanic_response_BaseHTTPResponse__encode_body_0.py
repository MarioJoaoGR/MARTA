
import pytest
from unittest.mock import patch
from sanic.response import BaseHTTPResponse

def test_init_basehttpresponse():
    with patch('sanic.response.BaseHTTPResponse.__init__', return_value=None):
        response = BaseHTTPResponse()
        assert not hasattr(response, 'asgi'), "Expected 'asgi' attribute to be False"


