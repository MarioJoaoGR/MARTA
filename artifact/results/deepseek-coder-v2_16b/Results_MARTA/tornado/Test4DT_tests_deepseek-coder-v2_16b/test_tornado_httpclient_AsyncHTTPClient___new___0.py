
import pytest
from tornado.httpclient import AsyncHTTPClient


def test_basic_usage():
    """Test basic usage of AsyncHTTPClient without force_instance and with default settings."""
    http_client = AsyncHTTPClient()
    assert isinstance(http_client, AsyncHTTPClient), "Instance should be an instance of AsyncHTTPClient"

