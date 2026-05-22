
import pytest
from unittest.mock import patch, MagicMock
from httpie.utils import ExplicitNullAuth

@pytest.fixture
def null_auth():
    return ExplicitNullAuth()

def test_valid_input(null_auth):
    # Create a mock HTTPRequest object
    request = MagicMock()
    
    # Call the __call__ method of the ExplicitNullAuth instance with the mock request
    result = null_auth(request)
    
    # Assert that the returned object is the same as the input object (no modification expected)
    assert result == request
