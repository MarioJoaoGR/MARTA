
import pytest
from semantic_release.hvcs import TokenAuth

# Test 1: Initialization of TokenAuth class
def test_tokenauth_initialization():
    token = "your_token_here"
    auth = TokenAuth(token)
    assert hasattr(auth, 'token')
    assert auth.token == token

# Test 2: Equality method for TokenAuth class
def test_tokenauth_equality():
    token1 = "token1"
    token2 = "token2"
    auth1 = TokenAuth(token1)
    auth2 = TokenAuth(token1)
    auth3 = TokenAuth(token2)
    
    assert auth1 == auth2
    assert not (auth1 == auth3)
