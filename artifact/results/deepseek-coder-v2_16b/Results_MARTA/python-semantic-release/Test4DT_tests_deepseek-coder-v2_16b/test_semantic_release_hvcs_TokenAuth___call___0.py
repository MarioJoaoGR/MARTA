
import pytest
from semantic_release.hvcs import TokenAuth
import requests

# Test initialization of TokenAuth class
def test_tokenauth_initialization():
    auth = TokenAuth("your_token_here")
    assert hasattr(auth, "token"), "Token should be a property of the TokenAuth instance"
    assert auth.token == "your_token_here", "The token should match the one provided during initialization"

# Test using TokenAuth in a request with requests library

# Test equality comparison of TokenAuth instances
def test_tokenauth_equality():
    auth1 = TokenAuth("same_token")
    auth2 = TokenAuth("same_token")
    assert auth1 == auth2, "Two instances with the same token should be considered equal"

# Test customizing a request object using __call__ method
def test_customizing_request():
    auth = TokenAuth("your_token_here")
    req = requests.Request('GET', 'https://api.example.com/data')
    prepared_req = auth(req)
    assert "Authorization" in prepared_req.headers, "Expected Authorization header to be added to the request headers"
    assert prepared_req.headers["Authorization"] == "token your_token_here", "The Authorization header should contain the token provided during initialization"