
import pytest
from unittest.mock import patch
from httpie.utils import ExplicitNullAuth

def test_invalid_input():
    # Create an instance of ExplicitNullAuth
    null_auth = ExplicitNullAuth()
    
    # Mock a request object
    class MockRequest:
        pass
    
    mock_request = MockRequest()
    
    # Call the __call__ method and check if it returns the same mocked request
    with patch('httpie.utils.ExplicitNullAuth.__init__', return_value=None):
        result = null_auth(mock_request)
        
        assert result == mock_request
