
import pytest
from unittest.mock import patch
from httpie.utils import ExplicitNullAuth

def test_none_input():
    # Create an instance of ExplicitNullAuth
    null_auth = ExplicitNullAuth()
    
    # Mock a request object
    class HTTPRequest:
        pass
    
    req = HTTPRequest()
    
    # Call the __call__ method and check if it returns the same request object
    with patch('httpie.utils.ExplicitNullAuth.__init__', return_value=None):
        result = null_auth(req)
        
    assert result == req
