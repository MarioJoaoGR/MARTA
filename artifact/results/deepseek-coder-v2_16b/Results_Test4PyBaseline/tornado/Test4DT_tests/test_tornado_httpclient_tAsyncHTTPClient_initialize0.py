
# Module: tornado.httpclient
import pytest
from unittest.mock import patch, MagicMock
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from typing import Dict, Any, Optional

# Mocking the necessary classes and functions for testing
class HTTPRequest:
    _DEFAULTS = {}

@patch('tornado.httpclient.IOLoop', autospec=True)
def test_initialize_with_defaults(mock_ioloop):
    client = AsyncHTTPClient()
    assert client.io_loop is mock_ioloop.current.return_value