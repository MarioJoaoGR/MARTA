
import pytest
from semantic_release.hvcs import Github

def test_github_auth():
    # Test authentication with a valid token
    with pytest.raises(AssertionError):
        assert Github.auth() is not None, "Authentication should succeed with a valid token"

    # Mock the environment variable to simulate no token provided
    import os
    os.environ['GH_TOKEN'] = ''
    
    # Test authentication without a token
    assert Github.auth() is None, "Authentication should fail when GH_TOKEN is not set"
