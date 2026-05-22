
import pytest
from unittest.mock import patch
from httpie.utils import ExplicitNullAuth

@pytest.fixture
def null_auth():
    return ExplicitNullAuth()

def test_none_input(null_auth):
    request = "some HTTP request"  # Replace with an actual request object if needed
    assert null_auth(request) == request
