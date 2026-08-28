
import pytest
from ansible.module_utils.urls import Request
import requests

# Fixture to create a request object with default settings for testing
@pytest.fixture
def default_request():
    return Request()

# Test cases for the `Request` class and its methods

def test_default_initialization(default_request):
    """Test initialization of Request without any parameters."""
    assert isinstance(default_request, Request)
    assert not default_request.headers
    assert default_request.use_proxy is True