
import pytest
from semantic_release.hvcs import TokenAuth

# Test initialization with a token
def test_tokenauth_initialization():
    auth = TokenAuth("your_token_here")
    assert hasattr(auth, "token"), "TokenAuth instance should have a 'token' attribute."
    assert auth.token == "your_token_here", "The initialized token should match the provided token."

# Test inequality comparison between two instances with different tokens
def test_tokenauth_inequality():
    auth1 = TokenAuth("token1")
    auth2 = TokenAuth("token2")
    assert auth1 != auth2, "Instances with different tokens should be considered unequal."

# Test equality comparison between two instances with the same token
def test_tokenauth_equality():
    auth1 = TokenAuth("same_token")
    auth2 = TokenAuth("same_token")
    assert auth1 == auth2, "Instances with the same tokens should be considered equal."

# Test inequality comparison between an instance and itself (should always return False)
def test_tokenauth_self_inequality():
    auth = TokenAuth("self_token")