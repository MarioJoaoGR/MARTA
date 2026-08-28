
import pytest
from semantic_release.hvcs import TokenAuth

# Test initialization with a token
def test_tokenauth_initialization():
    auth = TokenAuth(token='your_token_here')
    assert hasattr(auth, 'token'), "Token should be set during initialization"
    assert auth.token == 'your_token_here', "The provided token should match the initialized token"

# Test inequality comparison with another TokenAuth instance
def test_tokenauth_inequality():
    auth1 = TokenAuth(token='token1')
    auth2 = TokenAuth(token='token2')
    assert auth1 != auth2, "Two different instances of TokenAuth should not be equal"

# Test equality comparison with the same TokenAuth instance
def test_tokenauth_equality():
    auth1 = TokenAuth(token='same_token')
    auth2 = TokenAuth(token='same_token')
    assert auth1 == auth2, "Two instances of TokenAuth with the same token should be equal"
