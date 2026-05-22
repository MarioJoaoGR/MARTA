
import pytest
from unittest.mock import patch
from httpie.utils import ExplicitNullAuth

@pytest.fixture(scope="module")
def null_auth():
    return ExplicitNullAuth()

def test_none_input(null_auth):
    # Create a mock request object
    class MockRequest:
        pass
    
    mock_request = MockRequest()
    
    # Call the __call__ method of the null_auth instance with the mock request
    result = null_auth.__call__(mock_request)
    
    # Assert that the result is the same as the input (no modification expected)
    assert result == mock_request
